---
id: 41373252392731
title: "Connecting Klaviyo and Snowflake"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/41373252392731-Connecting-Klaviyo-and-Snowflake"
section: "Syncing"
category: "Advanced KDP & Marketing Analytics"
category_slug: "advanced-kdp-marketing-analytics"
klaviyo_updated: "2026-04-21T13:54:56Z"
language: en
---

[Advanced KDP](https://help.klaviyo.com/hc/en-us/articles/17655007276059) is not included in Klaviyo’s standard marketing application, and a subscription is required to access the associated functionality. Head to our [billing guide](https://help.klaviyo.com/hc/en-us/articles/115000976672) to learn about how to purchase this plan.

For the purposes of this article we use the term “table”, but views, materialized views, and tables are all valid Snowflake objects that can be imported. As long as Klaviyo can run SELECT col1 FROM table\_name on the object, you are free to use whatever you prefer.

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [RFC 2119](https://datatracker.ietf.org/doc/html/rfc2119).

## Snowflake Admin Setup

This section outlines the steps you must follow in your Snowflake environment to allow Klaviyo to import your data.

1. Generate a private key by running the following command in your local terminal:

   ```
   openssl genrsa 2048 | openssl pkcs8 -topk8 -inform PEM -out rsa_key.p8 -nocrypt
   ```
2. Generate a public key that references the private key by running the following command in your terminal:

   ```
   openssl rsa -in rsa_key.p8 -pubout -out rsa_key.pub
   ```
3. Copy the rsa\_key.pub and paste it into the script below to replace the placeholder ‘GENERATE\_PUBLIC\_KEY’ value for user\_rsa\_public\_key. The script below will work for Mac users, or you can open rsa\_key.pub in an IDE and copy the full contents of the file if you prefer.

   ```
   # Mac terminal command to write the key to your terminal and copy it to the clipboard
   cat rsa_key.pub | tee /dev/tty | pbcopy
   ```
4. Run the following script in your Snowflake environment to create a service user for Klaviyo to use. You must have securityadmin and sysadmin privileges in order to complete the setup below. To review what role(s) you have, run SHOW GRANTS TO USER <your\_username> and ensure that you have both roles listed. Reach out to a system administrator if you need to have your role adjusted.
   1. You should feel free to update any of the variables set at the beginning of the script.
   2. In summary, you’ll:
      1. Choose an existing warehouse or create a new one
      2. Choose an existing database or create a new one to hold the new schemas
      3. Create two new schemas `KLAVIYO_TMP`, and `KLAVIYO_IMPORT_FROM_DWH`
      4. Create a new network policy and allow list Klaviyo IPs
      5. Create a user and role for Klaviyo
   3. This script is idempotent (can be safely run multiple times), but will not overwrite existing objects with conflicting names.

```
BEGIN;

-- create variables for user / password / role / warehouse / database.
-- Change these to whatever you prefer.
SET role_name = 'KLAVIYO_DATA_TRANSFER_ROLE'; -- all letters must be uppercase, ex. 'KLAVIYO_DATA_TRANSFER_ROLE'
SET user_name = 'KLAVIYO_DATA_TRANSFER_USER'; -- all letters must be uppercase, ex. 'KLAVIYO_DATA_TRANSFER_USER'
SET warehouse_name = 'KLAVIYO_DATA_TRANSFER_WAREHOUSE'; -- all letters must be uppercase, ex. 'KLAVIYO_DATA_TRANSFER_WAREHOUSE'
SET database_name = 'KLAVIYO_DATABASE'; -- all letters must be uppercase, ex. 'KLAVIYO_DATABASE'. If this database doesn't exist, a new one will be created.
SET network_policy = 'KLAVIYO_DATA_TRANSFER_NETWORK_POLICY'; -- all letters must be uppercase, ex. 'KLAVIYO_NETWORK_POLICY'
SET network_rule = 'KLAVIYO_DATA_TRANSFER_NETWORK_RULE'; -- all letters must be uppercase, ex. 'KLAVIYO_NETWORK_RULE'
/* replace GENERATE_PUBLIC_KEY below with generated public key */

-- DO NOT CHANGE
SET schema_name_tmp = $database_name || '.KLAVIYO_TMP';  -- DO NOT CHANGE
SET schema_name_import = $database_name || '.KLAVIYO_IMPORT_FROM_DWH';  -- DO NOT CHANGE
SET full_network_rule_tmp = $schema_name_tmp || '.' || $network_rule; -- DO NOT CHANGE
SET full_network_rule_import = $schema_name_import || '.' || $network_rule; -- DO NOT CHANGE


-- change role to sysadmin for warehouse / database steps
USE ROLE sysadmin;

-- create a warehouse for data transfer service
CREATE WAREHOUSE IF NOT EXISTS IDENTIFIER($warehouse_name)
    warehouse_size = xsmall
    warehouse_type = standard
    auto_suspend = 60
    auto_resume = true
    initially_suspended = true;

-- create database for data transfer service
CREATE DATABASE IF NOT EXISTS IDENTIFIER($database_name);

-- create schemas for data transfer service
CREATE SCHEMA IF NOT EXISTS IDENTIFIER($schema_name_tmp);
CREATE SCHEMA IF NOT EXISTS IDENTIFIER($schema_name_import);

-- change role to securityadmin for user / role steps
USE ROLE securityadmin;

-- create network rule and policy for database
GRANT USAGE ON DATABASE IDENTIFIER($database_name) TO ROLE securityadmin;
GRANT USAGE, CREATE NETWORK RULE ON SCHEMA IDENTIFIER($schema_name_tmp) TO ROLE securityadmin;
GRANT USAGE, CREATE NETWORK RULE ON SCHEMA IDENTIFIER($schema_name_import) TO ROLE securityadmin;

-- whitelist klaviyo ip ranges, for KLAVIYO_TMP schema
CREATE NETWORK RULE IF NOT EXISTS IDENTIFIER($full_network_rule_tmp)
    type = IPV4
    value_list = (
        '184.72.183.187/32', '52.206.71.52/32', '3.227.146.32/32', '44.198.39.11/32', '35.172.58.121/32', '3.228.37.244/32', '54.88.219.8/32', '3.214.211.176/32'
        )
    comment = 'Klaviyo IP Ranges as of April 2025';
CREATE NETWORK POLICY IF NOT EXISTS IDENTIFIER($network_policy)
    allowed_network_rule_list = ($full_network_rule_tmp);

-- whitelist klaviyo ip ranges, for KLAVIYO_IMPORT_FROM_DWH schema
CREATE NETWORK RULE IF NOT EXISTS IDENTIFIER($full_network_rule_import)
    type = IPV4
    value_list = (
        '184.72.183.187/32', '52.206.71.52/32', '3.227.146.32/32', '44.198.39.11/32', '35.172.58.121/32', '3.228.37.244/32', '54.88.219.8/32', '3.214.211.176/32'
        )
    comment = 'Klaviyo IP Ranges as of April 2025';
CREATE NETWORK POLICY IF NOT EXISTS IDENTIFIER($network_policy)
allowed_network_rule_list = ($full_network_rule_import);


-- create role for data transfer service
CREATE ROLE IF NOT EXISTS IDENTIFIER($role_name);
GRANT ROLE IDENTIFIER($role_name) TO ROLE sysadmin;

-- create a user for data transfer service
CREATE USER IF NOT EXISTS IDENTIFIER($user_name)
    type = SERVICE
    network_policy = $network_policy
    default_role = $role_name
    default_warehouse = $warehouse_name
    rsa_public_key = 'GENERATE_PUBLIC_KEY';
GRANT ROLE IDENTIFIER($role_name) TO USER IDENTIFIER($user_name);
ALTER USER IDENTIFIER($user_name) SET NETWORK_POLICY = $network_policy;

-- grant service role access to warehouse
GRANT USAGE
    ON WAREHOUSE IDENTIFIER($warehouse_name)
    TO ROLE IDENTIFIER($role_name);

-- grant service access to database
GRANT MONITOR, USAGE
    ON DATABASE IDENTIFIER($database_name)
    TO ROLE IDENTIFIER($role_name);

-- Grant privileges for KLAVIYO_TMP
GRANT USAGE ON SCHEMA IDENTIFIER($schema_name_tmp) TO ROLE IDENTIFIER($role_name);
GRANT MONITOR, USAGE, CREATE TABLE, CREATE VIEW, CREATE SEQUENCE, CREATE FUNCTION, CREATE PROCEDURE
    ON SCHEMA IDENTIFIER($schema_name_tmp)
    TO ROLE IDENTIFIER($role_name);
GRANT ALL ON FUTURE TABLES IN SCHEMA IDENTIFIER($schema_name_tmp) TO ROLE IDENTIFIER($role_name);

-- Grant privileges for KLAVIYO_IMPORT_FROM_DWH
GRANT USAGE ON SCHEMA IDENTIFIER($schema_name_import) TO ROLE IDENTIFIER($role_name);
GRANT SELECT
    ON FUTURE TABLES
    IN SCHEMA IDENTIFIER($schema_name_import)
    TO ROLE IDENTIFIER($role_name);

COMMIT;
```

## Snowflake Data Setup

Above, you created two new schemas.

- KLAVIYO\_TMP will be used exclusively by Klaviyo. You MUST NOT modify any tables created in this schema. Klaviyo will delete these tables when they are no longer needed.
- KLAVIYO\_IMPORT\_FROM\_DWH is where you should store your final tables for Klaviyo to import. When you go through the sync creation process, all the tables in this schema will be listed for you to choose from. Hence you SHOULD only store the final tables you want to import to avoid confusion during setup.

All tables you plan to import to Klaviyo must meet the following criteria.

### Timestamp Requirements

1. Tables MUST contain a timestamp field that indicates when the row was created or updated. Often this will be inserted\_at or updated\_at. You will set this for each table during the sync creation process.
   1. The timestamp field MUST be monotonically increasing (i.e. it must always be getting larger or staying the same, never getting smaller).
   2. After sync creation, you MUST NOT set a row’s timestamp value to a time in the past or Klaviyo may not pick up that row.
   3. The timezone of this particular field is not important to Klaviyo, so long as you follow the above requirements
   4. Klaviyo RECOMMENDS you set the timestamp field with CURRENT\_TIMESTAMP() or an equivalent function. Multiple rows can have the same timestamp. See example below.

      ```
      INSERT INTO table_name AS

      SELECT ...

          , CURRENT_TIMESTAMP() AS inserted_at

      ...
      ```
2. Your timestamps MUST be in UTC, or include timezone information. If timezone information is missing, Klaviyo will assume UTC. For custom properties, these timestamps remain in string format, allowing you to interpret them in your preferred timezone.

### Table Structure

1. Tables SHOULD be treated as append-only (aka insert-only)
   1. If you prefer to update the rows in place instead, you MUST update the timestamp field so Klaviyo can identify the change.
2. Tables SHOULD be ordered on your timestamp column. Snowflake will handle clustering and partitioning based on your insert order. This will help optimize Klaviyo’s import queries, keeping compute costs in Snowflake down

### Profile Uniqueness and Consistency

1. You MUST ensure each profile property is imported from only one data source (table). Klaviyo prevents selecting the same property from different tables during sync creation, simplifying this requirement.
2. You SHOULD use the same profile identifier(s) (email, phone number, external ID, etc) in all your import tables, to minimize the risk of duplicate profiles being created.
   1. Klaviyo will create new profiles if the profile identifier you provide does not match an existing profile within Klaviyo.
   2. Example: Table1 (Email, fav\_color) + Table2 (Phone, birthday)
      1. This could create 2 profiles for the same person if the profile doesn’t currently exist. If a profile does exist, Klaviyo will handle the profile resolution and updates internally.
   3. One way to avoid this problem is to use only a single import table for all of your profiles.

### Circular Import-Export Loop Prevention

1. You SHOULD carefully manage scenarios where both import and export features are used to prevent circular import-export loops. Ensure your export process does not feed data back into a table that is upstream of your import table, as Klaviyo does not currently detect this scenario.
   1. Klaviyo does not yet have logic to detect this scenario.
   2. This would look something like:
      1. On each export sync cycle, Klaviyo will export all your profiles
      2. Then you add all of your exported profiles to your import table through some series of transformations.
      3. On each import sync cycle, Klaviyo will read all the profiles in your import table, which will eventually be re-exported
   3. Scenarios where this is probably safe
      1. if you are only using the export table to restrict the rows added to your import table
      2. If you verify the export table does not add rows to your import table.
   4. What are the consequences of a circular import-export loop?
      1. This will result in unnecessary compute costs for both you and Klaviyo.