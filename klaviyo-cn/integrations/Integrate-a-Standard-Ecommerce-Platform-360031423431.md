---
id: "360031423431"
title: "集成标准电子商务平台"
source_url: "https://help.klaviyo.com/hc/en-us/articles/360031423431-Integrate-a-Standard-Ecommerce-Platform"
section: "Custom integrations"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:44Z"
language: "zh"
translation_strategy: "google_html_text_nodes_preserve_attributes"
---
<h2>概述</h2>
<p>如果您已经构建了自己的自定义购物车解决方案，或者我们的预构建集成之一尚不支持您想要在 Klaviyo 中跟踪的电子商务数据，您可以使用我们的 <a href="https://www.klaviyo.com/docs/getting-started">JavaScript API</a>, <a href="https://www.klaviyo.com/docs/http-api">服务器端API</a>和自定义目录集成。</p>
<p>集成自定义电子商务购物车的关键组件是：</p>
<ul>
<li>客户资料</li>
<li>订阅者</li>
<li>网站活动</li>
<li>订单活动</li>
</ul>
<p>本指南重点介绍如何将重要指标或关键客户活动同步到 Klaviyo。虽然我们的 JavaScript 和服务器端跟踪和识别 API 可以互换使用，但我们建议电子商务企业使用以下设置。设置集成时将此用作清单：</p>
<ul>
<li>使用我们的 JavaScript Track API<em> </em>对于以下情况：
<ul>
<li>
<strong>现场活跃</strong> - 当有人访问您的网站时</li>
<li>
<strong>查看过的产品</strong> - 当有人查看产品时</li>
<li>
<strong>已添加到购物车</strong> - 当有人将商品添加到购物车时</li>
<li>
<strong>开始结账</strong> - 当有人登陆结账页面时</li>
</ul>
</li>
<li>使用我们的服务器端 Track API 执行以下操作：
<ul>
<li>
<strong>已下订单</strong> - 当订单在您的系统上成功处理时</li>
<li>
<strong>订购产品</strong> - 已处理订单中每个项目的事件</li>
<li>
<strong>已履行订单</strong> - 当订单发送给客户时</li>
<li>
<strong>取消订单</strong> - 当客户取消订单时</li>
<li>
<strong>已退款订单</strong> - 当客户的订单退款时</li>
</ul>
</li>
<li>使用我们的自定义目录 Feed 集成可实现以下目的：
<ul>
<li>
<strong>目录提要</strong> - 产品目录的 XML feed 或 JSON feed</li>
</ul>
</li>
</ul>
<p>您在这些网站、购买和结帐事件中发送到 Klaviyo 的详细数据级别将决定您如何根据 Klaviyo 中的这些事件进行过滤和细分。要了解必须如何构建数据以便关键事件详细信息可用于细分， <a href="https://help.klaviyo.com/hc/en-us/articles/115005062847-Understand-the-Data-Available-for-Segmentation">查看我们的航段条件指南</a>.</p>
<p>请注意，本指南中的片段使用示例数据。您将需要更新这些代码片段中的 JSON 属性的值，以便它们动态地从该属性所需的相关信息中提取。</p>
<p>请务必查看我们的 <a href="https://help.klaviyo.com/hc/en-us/articles/360031078492" target="_self">定制集成常见问题解答</a> 有关自定义集成的任何问题或 <a href="https://help.klaviyo.com/hc/en-us/requests/new" target="_self">联系我们的支持团队</a>.</p>
<h2>现场行为（JavaScript Track API）</h2>
<p>要启用我们的 JavaScript API 以及直接从 Klaviyo 向您的网站发布表单的能力，请添加以下代码片段，以便显示在您网站的每个页面上（通常页脚的末尾是添加此代码的好地方）。确保将 PUBLIC_API_KEY 替换为您的 Klaviyo 帐户的 6 个字符 <a href="https://www.klaviyo.com/account#api-keys-tab">公共 API 密钥</a>:</p>
<pre><code class="language-js">&lt;script type="application/javascript" async
src="https://static.klaviyo.com/onsite/js/klaviyo.js?company_id=PUBLIC_API_KEY"&gt;&lt;/script&gt;</code></pre>
<h3>现场活跃</h3>
<p>添加上面的代码片段后， <strong>现场活跃</strong> 现在，任何接受 cookie 的人都会触发活动：</p>
<ul>
<li>出发至 <a href="https://help.klaviyo.com/hc/en-us/articles/115000751052-Klaviyo-API-Reference-Guide#identifying-users--javascript-3">Javascript 识别 API 请求</a>
</li>
<li>通过 Klaviyo 表格注册</li>
<li>点击 Klaviyo 电子邮件并登陆您的网站</li>
</ul>
<h3>查看过的产品</h3>
<p>如果您想设置一个 <a href="https://help.klaviyo.com/hc/en-us/articles/115002775252-Create-a-Browse-Abandonment-Flow">浏览放弃流程</a> 或者根据产品浏览数据构建细分，您需要添加 JavaScript 事件跟踪 <strong>查看过的产品</strong> 公制。在您的产品页面模板上，添加以下代码段：</p>
<pre><code class="language-js">&lt;script text="text/javascript"&gt;
   var _learnq = _learnq || [];
   var item = {
     "ProductName": "Winnie the Pooh",
     "ProductID": "1111",
     "Categories": ["Fiction", "Children"],
     "ImageURL": "http://www.example.com/path/to/product/image.png",
     "URL": "http://www.example.com/path/to/product",
     "Brand": "Kids Books",
     "Price": 9.99,
     "CompareAtPrice": 14.99
   };
 
   _learnq.push(["track", "Viewed Product", item]);
 
   _learnq.push(["trackViewedItem", {
     Title: item.ProductName,
     ItemId: item.ProductID,
     Categories: item.Categories,
     ImageUrl: item.ImageURL,
     Url: item.URL,
     Metadata: {
       Brand: item.Brand,
       Price: item.Price,
       CompareAtPrice: item.CompareAtPrice
     }
   }]);
 &lt;/script&gt;</code></pre>
<h3>已添加到购物车</h3>
<p>如果您想发送废弃购物车电子邮件 <em>前</em> 当有人登陆结帐页面时，您需要在有人执行特定操作时跟踪有关购物车的信息。为此，我们建议发送一个 <strong>已添加到购物车</strong> 当有人将商品添加到购物车时发生的事件。一个人仍然需要经过“身份识别”或 cookie 处理才能跟踪此事件。对于有效负载，您应该包含所有购物车信息（例如 <strong>开始结账</strong> 如下）以及有关刚刚添加的商品的信息（如上面查看的产品）。这是跟踪请求的示例：</p>
<pre><code class="language-js">&lt;script text="text/javascript"&gt;
   _learnq.push(['track', Added to Cart, {
     "$value": 29.98,
     "AddedItemProductName": "A Tale of Two Cities",
     "AddedItemProductID": "1112",
     "AddedItem_SKU": "TALEOFTWO",
     "AddedItem_Categories": ["Fiction", "Classics"],
     "AddedItem_ImageURL": "http://www.example.com/path/to/product/image2.png",
     "AddedItem_URL": "http://www.example.com/path/to/product2",
     "AddedItem_Price": 19.99,
     "AddedItem_Quantity": 1,
     "ItemNames": ["Winnie the Pooh", "A Tale of Two Cities"],
     "CheckoutURL": "http://www.example.com/path/to/checkout",
     "Items": [{
         "ProductID": "1111",
         "SKU": "WINNIEPOOH",
         "ProductName": "Winnie the Pooh",
         "Quantity": 1,
         "ItemPrice": 9.99,
         "RowTotal": 9.99,
         "ProductURL": "http://www.example.com/path/to/product",
         "ImageURL": "http://www.example.com/path/to/product/image.png",
         "ProductCategories": ["Fiction", "Children"]
       },
       {
         "ProductID": "1112",
         "SKU": "TALEOFTWO",
         "ProductName": "A Tale of Two Cities",
         "Quantity": 1,
         "ItemPrice": 19.99,
         "RowTotal": 19.99,
         "ProductURL": "http://www.example.com/path/to/product2",
         "ImageURL": "http://www.example.com/path/to/product/image2.png",
         "ProductCategories": ["Fiction", "Classics"]
       }
     ]
   }]);
 &lt;/script&gt;</code></pre>
<h3>开始结账</h3>
<p>如果您想发送，结帐数据很重要 <a href="https://help.klaviyo.com/hc/en-us/articles/115002779411-Guide-to-Creating-an-Abandoned-Cart-Flow">废弃的结帐电子邮件</a>。当有人开始结帐流程时，您将向 Klaviyo 发送一个事件，指示他们开始结帐。触发此事件的最佳位置是当某人在被“识别”后访问结账页面时，或者当他们在结账页面上输入电子邮件地址（如果尚未被识别）时。</p>
<p>您需要确保包含订单项的所有详细信息，以便可以自定义放弃的结账电子邮件，以包含有关某人购物车中产品的图片、链接和其他信息。这是跟踪请求的示例：</p>
<pre><code class="language-js">&lt;script text="text/javascript"&gt;
   _learnq.push(['track', 'Started Checkout', {
     "$event_id": "1000123_1387299423",
     "$value": 29.98,
     "ItemNames": ["Winnie the Pooh", "A Tale of Two Cities"],
     "CheckoutURL": "http://www.example.com/path/to/checkout",
     "Items": [{
         "ProductID": "1111",
         "SKU": "WINNIEPOOH",
         "ProductName": "Winnie the Pooh",
         "Quantity": 1,
         "ItemPrice": 9.99,
         "RowTotal": 9.99,
         "ProductURL": "http://www.example.com/path/to/product",
         "ImageURL": "http://www.example.com/path/to/product/image.png",
         "ProductCategories": ["Fiction", "Children"]
       },
       {
         "ProductID": "1112",
         "SKU": "TALEOFTWO",
         "ProductName": "A Tale of Two Cities",
         "Quantity": 1,
         "ItemPrice": 19.99,
         "RowTotal": 19.99,
         "ProductURL": "http://www.example.com/path/to/product2",
         "ImageURL": "http://www.example.com/path/to/product/image2.png",
         "ProductCategories": ["Fiction", "Classics"]
       }
     ]
   }]);
 &lt;/script&gt;</code></pre>
<p>这 <code class="language-html">$event_id</code> 应是购物车的唯一标识符与触发事件时的 UNIX 格式时间相结合。这允许某人触发 <strong>开始结账</strong> 当他们在添加其他物品后返回时不止一次。</p>
<h2>服务器端指标</h2>
<p>由于前端代码的潜在限制以及安全问题，我们建议在服务器端跟踪某些指标。如果某人的连接/计算机速度较慢或浏览器上存在 JavaScript 阻止插件，则 JavaScript 请求可能不会触发。对于更重要的指标（例如订单和其他交易事件和属性的指标）或包含敏感数据的指标，请使用我们的服务器端跟踪和识别 API。</p>
<h3>已下订单</h3>
<p>下订单后，您应该向我们提出跟踪请求 <a href="https://www.klaviyo.com/docs">服务器端API</a>。我们有图书馆可供使用 <a href="https://github.com/klaviyo/python-klaviyo">Python</a>, <a href="https://github.com/klaviyo/ruby-klaviyo">红宝石</a>， 和 <a href="https://github.com/klaviyo/php-klaviyo">PHP</a>，但一般来说，API 只需要使用 base64 编码的 JSON 负载发出 HTTP GET 请求。</p>
<div class="bs-callout bs-callout-default">
<p>发送历史订单数据也是一个很好的做法。这将增强您细分数据的能力并提高收入跟踪的历史准确性。历史数据可以通过迭代您的历史订单并生成来发送给我们 <strong>已下订单</strong> 和 <strong>订购产品</strong> 跟踪每个 API 请求。这些事件的特殊“时间”属性应该是该订单发生时的 UNIX 时间戳。  有关这些指标的更多详细信息如下。</p>
</div>
<p>您需要通过以下两种方式之一将订单数据发送到 Klaviyo：实时或批量。</p>
<ul>
<li>
<strong> 即时的 -</strong> 下订单后您将立即提出请求</li>
<li>
<strong> 批 -</strong> 您将编写一个每小时至少运行一次的脚本，以发送过去一小时内发生的所有事件</li>
</ul>
<p>如果您打算发送废弃的购物车/结账电子邮件，则需要至少以电子邮件延迟范围内的频率发送订单数据，以阻止电子邮件发送给已完成订单的人。例如，如果有人触发废弃购物车流程与他们收到第一封电子邮件之间有一个小时的时间延迟，则您需要确保每小时至少发送一次数据。</p>
<p>For each order, we recommend you send two types of events:</p>
<ul>
<li>一项名为 <strong>已下订单</strong> 对于整个订单
<ul>
<li>这包括一个 <code class="language-html">$value</code> 代表整个订单总价值的属性，包括运费、税费、折扣等。</li>
</ul>
</li>
<li>每个名为的行项目一个事件 <strong>订购产品</strong>
<ul>
<li>这包括一个 <code class="language-html">$value</code> 属性，表示订单中商品在进行任何调整之前的总成本以及有关该商品的更多 SKU 级别的详细信息</li>
</ul>
</li>
</ul>
<p>跟踪服务器端事件时需要注意的关键事项：</p>
<ul>
<li>确保更换 <code class="language-html">API_KEY</code> 和 <a href="https://www.klaviyo.com/account#api-keys-tab">您的公共 API 密钥</a>.</li>
<li>这 <code class="language-html">$event_id</code> 应是订单的唯一标识符（例如订单 ID）。</li>
<li>如果相同的组合 <code class="language-html">event</code> 和 <code class="language-html">$event_id</code> 发送多次，我们将跳过第一个具有相同组合的跟踪事件。</li>
<li>
<code class="language-html">$value</code> 是一种特殊属性，允许 Klaviyo 跟踪收入；这应该是与其相关的事件的总数字、货币价值。</li>
<li>“Items”数组应包含每个行项目的一个字典。</li>
<li>
<code class="language-html">time</code> 是一个特殊属性，应该是订单日期和时间的 UNIX 时间戳。</li>
</ul>
<p>这是跟踪请求的示例 <strong>已下订单</strong>:</p>
<pre><code class="language-json">{
   "token": "API_KEY",
   "event": "Placed Order",
   "customer_properties": {
     "$email": "john.smith@example.com",
     "$first_name": "John",
     "$last_name": "Smith",
     "$phone_number": "5551234567",
     "$address1": "123 Abc st",
     "$address2": "Suite 1",
     "$city": "Boston",
     "$zip": "02110",
     "$region": "MA",
     "$country": "USA"
   },
   "properties": {
     "$event_id": "1234",
     "$value": 29.98,
     "Categories": ["Fiction", "Classics", "Children"],
     "ItemNames": ["Winnie the Pooh", "A Tale of Two Cities"],
     "Brands": ["Kids Books", "Harcourt Classics"],
     "Discount Code": "Free Shipping",
     "Discount Value": 5,
     "Items": [{
         "ProductID": "1111",
         "SKU": "WINNIEPOOH",
         "ProductName": "Winnie the Pooh",
         "Quantity": 1,
         "ItemPrice": 9.99,
         "RowTotal": 9.99,
         "ProductURL": "http://www.example.com/path/to/product",
         "ImageURL": "http://www.example.com/path/to/product/image.png",
         "Categories": ["Fiction", "Children"],
         "Brand": "Kids Books"
       },
       {
         "ProductID": "1112",
         "SKU": "TALEOFTWO",
         "ProductName": "A Tale of Two Cities",
         "Quantity": 1,
         "ItemPrice": 19.99,
         "RowTotal": 19.99,
         "ProductURL": "http://www.example.com/path/to/product2",
         "ImageURL": "http://www.example.com/path/to/product/image2.png",
         "Categories": ["Fiction", "Classics"],
         "Brand": "Harcourt Classics"
       }
     ]
   },
   "time": 1387302423
 }</code></pre>
<h3>订购产品</h3>
<p>对于每个订单项，您还应该发出跟踪请求 <strong>订购产品</strong> 事件：</p>
<pre><code class="language-json">{
   "token": "API_KEY",
   "event": "Ordered Product",
   "customer_properties": {
     "$email": "john.smith@example.com",
     "$first_name": "John",
     "$last_name": "Smith"
   },
   "properties": {
     "$event_id": "1234_WINNIEPOOH",
     "$value": 9.99,
     "ProductID": "1111",
     "SKU": "WINNIEPOOH",
     "ProductName": "Winnie the Pooh",
     "Quantity": 1,
     "ProductURL": "http://www.example.com/path/to/product",
     "ImageURL": "http://www.example.com/path/to/product/image.png",
     "ProductCategories": [
       "Fiction",
       "Children"
     ],
     "ProductBrand": "Kids Books"
   },
   "time": 1387302423
 }</code></pre>
<h3>已履行的订单、已取消的订单和已退款的订单</h3>
<p>Depending on how your products are sent to the customer, or whether they are able to be cancelled or refunded, you may want to send additional events that reflect these actions. Each of these order-related events will have almost the same payload as a <strong>已下订单</strong> 事件。</p>
<p>为了 <strong>已履行订单</strong>，唯一要更新的是事件名称和履行发生的时间：</p>
<pre><code class="language-json">{
   "token": "API_KEY",
   "event": "Fulfilled Order",
   "customer_properties": {
     "$email": "john.smith@example.com",
     "$first_name": "John",
     "$last_name": "Smith",
     "$phone_number": "5551234567",
     "$address1": "123 Abc st",
     "$address2": "Suite 1",
     "$city": "Boston",
     "$zip": "02110",
     "$region": "MA",
     "$country": "USA"
   },
   "properties": {
     "$event_id": "1234",
     "$value": 29.98,
     "Categories": [
       "Fiction",
       "Classics",
       "Children"
     ],
     "ItemNames": [
       "Winnie the Pooh",
       "A Tale of Two Cities"
     ],
     "Brands": [
       "Kids Books",
       "Harcourt Classics"
     ],
     "Discount Code": "Free Shipping",
     "Discount Value": 5,
     "Items": [
       {
         "ProductID": "1111",
         "SKU": "WINNIEPOOH",
         "ProductName": "Winnie the Pooh",
         "Quantity": 1,
         "ItemPrice": 9.99,
         "RowTotal": 9.99,
         "ProductURL": "http://www.example.com/path/to/product",
         "ImageURL": "http://www.example.com/path/to/product/image.png",
         "Categories": [
           "Fiction",
           "Children"
         ],
         "Brand": "Kids Books"
       },
       {
         "ProductID": "1112",
         "SKU": "TALEOFTWO",
         "ProductName": "A Tale of Two Cities",
         "Quantity": 1,
         "ItemPrice": 19.99,
         "RowTotal": 19.99,
         "ProductURL": "http://www.example.com/path/to/product2",
         "ImageURL": "http://www.example.com/path/to/product/image2.png",
         "Categories": [
           "Fiction",
           "Classics"
         ],
         "Brand": "Harcourt Classics"
       }
     ]
   },
   "time": 1387312956
 }</code></pre>
<p>为了 <strong>取消订单</strong> 和 <strong>已退款订单</strong>，更新事件名称和时间戳并添加取消或退款原因的附加属性：</p>
<h4>取消订单</h4>
<pre><code class="language-json">
   "token": "API_KEY",
   "event": "Cancelled Order",
   "customer_properties": {
     "$email": "john.smith@example.com",
     "$first_name": "John",
     "$last_name": "Smith",
     "$phone_number": "5551234567",
     "$address1": "123 Abc st",
     "$address2": "Suite 1",
     "$city": "Boston",
     "$zip": "02110",
     "$region": "MA",
     "$country": "USA"
   },
   "properties": {
     "$event_id": "1234",
     "$value": 29.98,
     "Reason": "No longer needed",
     "Categories": [
       "Fiction",
       "Classics",
       "Children"
     ],
     "ItemNames": [
       "Winnie the Pooh",
       "A Tale of Two Cities"
     ],
     "Brands": [
       "Kids Books",
       "Harcourt Classics"
     ],
     "Discount Code": "Free Shipping",
     "Discount Value": 5,
     "Items": [
       {
         "ProductID": "1111",
         "SKU": "WINNIEPOOH",
         "ProductName": "Winnie the Pooh",
         "Quantity": 1,
         "ItemPrice": 9.99,
         "RowTotal": 9.99,
         "ProductURL": "http://www.example.com/path/to/product",
         "ImageURL": "http://www.example.com/path/to/product/image.png",
         "Categories": [
           "Fiction",
           "Children"
         ],
         "Brand": "Kids Books"
       },
       {
         "ProductID": "1112",
         "SKU": "TALEOFTWO",
         "ProductName": "A Tale of Two Cities",
         "Quantity": 1,
         "ItemPrice": 19.99,
         "RowTotal": 19.99,
         "ProductURL": "http://www.example.com/path/to/product2",
         "ImageURL": "http://www.example.com/path/to/product/image2.png",
         "Categories": [
           "Fiction",
           "Classics"
         ],
         "Brand": "Harcourt Classics"
       }
     ]
   },
   "time": 1387312956
 }</code></pre>
<h4>已退款订单</h4>
<pre><code class="language-json">{
   "token": "API_KEY",
   "event": "Refunded Order",
   "customer_properties": {
     "$email": "john.smith@example.com",
     "$first_name": "John",
     "$last_name": "Smith",
     "$phone_number": "5551234567",
     "$address1": "123 Abc st",
     "$address2": "Suite 1",
     "$city": "Boston",
     "$zip": "02110",
     "$region": "MA",
     "$country": "USA"
   },
   "properties": {
     "$event_id": "1234",
     "$value": 29.98,
     "Reason": "No longer needed",
     "Categories": [
       "Fiction",
       "Classics",
       "Children"
     ],
     "ItemNames": [
       "Winnie the Pooh",
       "A Tale of Two Cities"
     ],
     "Brands": [
       "Kids Books",
       "Harcourt Classics"
     ],
     "Discount Code": "Free Shipping",
     "Discount Value": 5,
     "Items": [
       {
         "ProductID": "1111",
         "SKU": "WINNIEPOOH",
         "ProductName": "Winnie the Pooh",
         "Quantity": 1,
         "ItemPrice": 9.99,
         "RowTotal": 9.99,
         "ProductURL": "http://www.example.com/path/to/product",
         "ImageURL": "http://www.example.com/path/to/product/image.png",
         "Categories": [
           "Fiction",
           "Children"
         ],
         "Brand": "Kids Books"
       },
       {
         "ProductID": "1112",
         "SKU": "TALEOFTWO",
         "ProductName": "A Tale of Two Cities",
         "Quantity": 1,
         "ItemPrice": 19.99,
         "RowTotal": 19.99,
         "ProductURL": "http://www.example.com/path/to/product2",
         "ImageURL": "http://www.example.com/path/to/product/image2.png",
         "Categories": [
           "Fiction",
           "Classics"
         ],
         "Brand": "Harcourt Classics"
       }
     ]
   },
   "time": 1387312956
 }</code></pre>
<h2>目录提要集成</h2>
<p>集成您的目录将允许您使用我们的 <a href="https://help.klaviyo.com/hc/en-us/articles/115005082787-Product-Feeds-and-Recommendations">产品提要</a> 和 <a href="https://help.klaviyo.com/hc/en-us/articles/115000219092-Insert-a-Product-Block">产品块</a> 在电子邮件中。要设置自定义目录集成，请联系我们 <a href="mailto:success@klaviyo.com">支持团队</a>。他们将传递此设置的文档和示例，并且需要在设置完成后收到通知才能激活您帐户上的源。</p>
<h2>同步历史数据</h2>
<p>将您的历史订单数据也发送给我们也是一个很好的做法。这将增强您细分数据的能力并提高收入跟踪的历史准确性。该数据可以通过迭代您的历史订单并生成来发送给我们 <strong>Placed Order</strong> 和 <strong>订购产品</strong> 跟踪每个 API 请求。</p>