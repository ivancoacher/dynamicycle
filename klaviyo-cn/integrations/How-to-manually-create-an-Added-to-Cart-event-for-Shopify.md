---
id: "115001396711"
title: "如何为 Shopify 手动创建“添加到购物车”事件"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115001396711-How-to-manually-create-an-Added-to-Cart-event-for-Shopify"
section: "Shopify best practices"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-05-11T11:00:04Z"
language: "zh"
---
## 你将会学到

了解如何为 Shopify 手动创建 **添加到购物车** 事件，以跟踪客户何时将商品添加到购物车，您可以使用该事件触发放弃的购物车流程。 Klaviyo 现在提供 **添加到购物车** 事件，[启用后通过我们的 Shopify 集成自动同步](https://help.klaviyo.com/hc/en-us/articles/4425956184731)，并且是 Shopify 品牌的。我们建议使用品牌事件，因为它是由 Klaviyo 积极维护的。如果您不想使用我们的自动事件，本文将详细介绍如何使用代码片段手动创建事件，该事件将通过齿轮图标同步到 Klaviyo。 **添加到购物车**与 Klaviyo 的 **结帐开始** 事件不同。 **结帐开始** 在客户将商品添加到购物车、在结帐过程中输入电子邮件并继续结帐后触发。这种情况发生在漏斗的更深处，而**添加到购物车**会在客户将商品添加到购物车时立即触发。 ## 开始之前

- 在继续阅读本文之前，请阅读我们的文章[Shopify 入门](https://help.klaviyo.com/hc/en-us/articles/115005080407-How-to-Integrate-with-Shopify)，了解有关集成的分步说明。 - 确保您已启用 [Klaviyo 现场跟踪](https://help.klaviyo.com/hc/en-us/articles/4425956184731)（包括查看的产品跟踪），以便“添加到购物车”活动正常运行。 - 请注意，“添加到购物车”事件仅跟踪用户[之前由 Klaviyo 进行 cookie](https://help.klaviyo.com/hc/en-us/articles/115005076767-Guide-to-Klaviyo-Onsite-Tracking#who-klaviyo-tracks5)。根据您在 Shopify 中的客户隐私设置，Klaviyo 可能不会跟踪欧盟、欧洲经济区、英国和瑞士的 Shopify 商店访客的现场活动，除非他们同意。 ## 创建“添加到购物车”事件

创建 **添加到购物车** 事件有 3 个步骤：

1. 选择放置代码片段的位置
2. 将代码片段添加到您的商店
3.测试代码片段

## 我应该将代码片段粘贴到哪里？确保将代码片段粘贴到您的默认产品页面以及您可能拥有的任何其他产品页面中。 ### 如果您的商店有自定义液体块，您应该使用一个作为代码片段

1. 在 Shopify 中，导航至****在线商店 > 主题****。 2. 找到您的主题并单击****自定义****。 3. 在页面顶部，单击****主页****下拉列表。 4. 选择****产品 > 默认产品**** 以进入默认产品页面。 5. 单击左侧边栏中的****添加部分****，然后选择****自定义液体****。 6. 将提供的代码片段粘贴到框中。 7. 单击右上角的****保存****。 8. 在左侧边栏中，**已添加到购物车** 的新自定义液体块应自动显示在页面上其他部分的下方。 - 如果您的 **已添加到购物车** 块需要移动，请将鼠标悬停在该块上，然后单击 6 个点将其拖动到其他部分下方


     ![Shopify 产品页面部分层次结构，包含两个自定义液体部分，其中一个显示六个灰点，位于其他产品部分下方](https://fast.wistia.com/embed/medias/3up33yx3rq/swatch)

### 如果您的商店没有自定义液体块，您应该将代码片段放入您的 theme.liquid 文件中

1. 在 Shopify 中，导航至****在线商店 > 主题****。 2. 找到您的主题并单击****自定义****。 3. 单击顶部的三个点并选择****编辑代码****。 4. 打开****theme.liquid**** 文件。 5. 将提供的代码片段粘贴到所有其他代码之后、结束“</body>”标记之前。 ![Shopify 中的 Theme.liquid 文件显示文本：在此处添加以蓝色突出显示的代码片段，后跟 </body](https://klaviyo.zendesk.com/hc/article_attachments/28711660840475)
6. 在代码片段上方，添加以下开始标记：“{% if product %}”
   ![Shopify 中的 Theme.liquid 文件显示产品标签是否以蓝色突出显示，后跟文本“在此处添加片段”，后跟 </body>](https://klaviyo.zendesk.com/hc/article_attachments/28711660843675)
7. 直接在代码片段之后添加以下结束标记：`{% endif %}`
8. 您的文件应如下所示：
   ![Shopify 中的 Theme.liquid 文件显示产品和 endif 标签是否围绕文本阅读添加片段，后跟 </body>](https://klaviyo.zendesk.com/hc/article_attachments/28711660847003)
9. 单击****保存****。 ## 将代码片段添加到您的网站

以下 **添加到购物车** 代码段应该适用于大多数 Shopify 商店。 每个 Shopify 商店都是不同的。如果您尝试下面的代码片段并进行测试，但它不起作用，您可以随时尝试“遇到问题？”下提供的备份代码片段。下面的下拉菜单。将以下代码段添加到您在上面确定的位置的 Shopify 商店。 ````
<脚本>
  window.addEventListener('加载', function() {
  var _learnq = window._learnq || []；
  函数添加到购物车（）{
   fetch(`${window.location.origin}/cart.js`)
   .then(res => res.clone().json().then(data => {
    var 购物车 = {
      总价格：data.总价格/100，
      $值：data.total_price/100,
      总折扣：data.total_discount，
      原始总价：data.original_total_price/100，
      项目：数据.项目
    }
    if (项目!== '未定义') {
      购物车 = Object.assign(购物车, 商品)
    }
    如果（klAjax）{
       _learnq.push(['track', '已添加到购物车', cart]);
       klAjax=假；
      }
   }））
  };
  （函数（ns，获取）{
    ns.fetch = 函数() {
      const 响应 = fetch.apply(this, 参数);
      响应.then(res => {
        if (`${window.location.origin}/cart/add.js`
          .includes(res.url) && res.url !== '') {
              添加到购物车（）
        }
      });
      返回响应
     }
  }(窗口, window.fetch));
  var klAjax = true;
  var atcButtons = document.querySelectorAll("form[action*='/cart/add'] button[type='submit']");
  for (var i = 0; i < atcButtons.length; i++) {
    atcButtons[i].addEventListener("点击", function() {
      如果（klAjax）{
        _learnq.push(['track', '已添加到购物车', item]);
        klAjax=假；
      }
    })
  }
  });
</脚本>
````

完成后，请使用下一节中的说明测试事件。 ## 测试您的“添加到购物车”事件

需要注意的是，Klaviyo 仅跟踪“已知浏览器”或已被 cookie 的浏览器（通过点击电子邮件、填写表格等）。因此，**添加到购物车**事件可能不会像您预期的那样很快出现在您的帐户中。要了解有关 Klaviyo 跟踪对象的更多信息，请参阅我们的[有关现场跟踪的文章](https://help.klaviyo.com/hc/en-us/articles/115005076767-Getting-started-with-Klaviyo-onsite-tracking#who-klaviyo-tracks5)。为了测试您的 **添加到购物车** 事件，您需要手动 cookie 您的电子邮件地址。请按照下列步骤操作：

1. 导航到您的网站。 2. 在您的主页上，将以下内容添加到网址末尾，并将 **testing.email@gmail.com** 替换为您的电子邮件地址：
   **?utm\_email=testing.email@gmail.com
   ![Shopify 测试商店，URL 附加 ?utm_email=example@gmail.com](https://klaviyo.zendesk.com/hc/article_attachments/28711673004699)**
3. 重新加载页面。 4. 导航到您网站上的产品页面，然后单击 **添加到购物车** 按钮。 5. 在 Klaviyo 中搜索您的电子邮件地址。 ![Klaviyo 仪表板的顶角，搜索栏中带有testing.email@gmail.com](https://klaviyo.zendesk.com/hc/article_attachments/28711673006235)

您应该看到已为您创建了 Klaviyo 个人资料（如果尚不存在），并且已在您的活动源中跟踪了此 **添加到购物车** 事件。 ## 使用给定代码片段跟踪添加到购物车时遇到问题？如果您在使用给定代码段跟踪 **添加到购物车** 时遇到问题，您可以尝试下面的 2 个附加代码段，我们将其称为 **代码段 2** 和 **代码段 3**。在测试新的代码片段之前，请确保首先删除不起作用的代码片段。 ### 确定要尝试的备份片段

您的商店是否使用按钮 ID 来定义 **添加到购物车** 按钮？如果答案是肯定的，请尝试 Snippet 2。如果您的 **Add to Cart** 按钮是由类表示法定义的，则应使用 Snippet 3。以下是如何确定您的商店是否使用按钮 ID 或类表示法的方法：

1. 1. 打开您网站的产品页面之一。 2. 右键单击​​“添加到购物车”按钮，然后选择****检查****。 3. 控制台将打开，并在控制台的 **Elements** 选项卡中显示“添加到购物车”按钮的源代码。 4. 在 **Elements** 选项卡中，您的代码可能如下所示：
      ![左侧有咖啡袋的产品页面，控制台打开到“元素”选项卡，“添加到购物车”上方弹出检查元素，控制台中突出显示按钮代码](https://klaviyo.zendesk.com/hc/article_attachments/28711672966299)
   5. 请注意，这个“添加到购物车”按钮没有按钮 ID（其中包括类似“id =”button_ID_name“”的内容）；相反，它由类符号引用（`class=“btn Product-form_cart-submit
      btn – 次重音"`)。 ### 片段 2

如果您的 **添加到购物车** 按钮是由按钮 ID 定义的，请将下面的代码段添加到您在“我应该将代码段放在哪里？”中确定的位置的 Shopify 商店中。部分，以及任何需要的标签。 ````
<脚本类型=“文本/javascript”>
var _learnq = _learnq || []；
	document.getElementById("AddToCart").addEventListener('click',function (){
 		_learnq.push(['track', '已添加到购物车', item]);
	});
</脚本>
````

此代码段可能需要修改，因为代码段中的 **Add to Cart** 变量需要与您网站上使用的按钮 ID 相匹配。 **添加到购物车** 变量的默认名称为“AddToCart”，在下面的代码片段中突出显示：
![Klaviyo 的“添加到购物车”片段，其中“添加到购物车”按钮 ID 以黄色突出显示](https://klaviyo.zendesk.com/hc/article_attachments/28711672969115)

检查按钮 ID 所需的步骤与检查网站上是否存在按钮 ID 相同：

1. 打开您网站的产品页面之一。 2. 右键单击​​“添加到购物车”按钮并选择****检查****。 3. 控制台将打开，显示“添加到购物车”按钮的源代码。下图显示了控制台中突出显示的“添加到购物车”按钮的 ID。 ![控制台中添加到购物车按钮代码，ID 等于 addToCart-product-template](https://klaviyo.zendesk.com/hc/article_attachments/28711672971931)
   此处显示的页面上按钮的 ID (`addToCart-product-template`) 与默认代码段中的变量 (`AddToCart`) 不同。 4. 如果不匹配，请修改代码片段以匹配按钮的 ID。我们的示例的修改后的代码片段如下所示：
   ![Klaviyo 的添加到购物车代码段由按钮 ID 定义，添加到购物车变量修改为 addToCart-product-template](https://klaviyo.zendesk.com/hc/article_attachments/28711672975003)

### 片段 3

如果您的 **添加到购物车** 按钮是通过类别符号定义的，请将下面的代码段添加到您在“我应该将代码段放在哪里？”中确定的位置的 Shopify 商店中。部分，以及任何需要的标签。 ````
<脚本类型=“文本/javascript”>
var _learnq = _learnq || []；
  var classname = document.getElementsByClassName("添加到购物车");
var addToCart = 函数() {
_learnq.push(['track', '已添加到购物车', item]);
}; for (var i = 0; i < 类名.length; i++) {
classname[i].addEventListener('click', addToCart, false);
}
</脚本>
````

此代码段可能需要修改，因为代码段中的 **Add to Cart** 变量需要与您网站上使用的类相匹配。 1. 打开您网站的产品页面之一。 2. 右键单击​​“添加到购物车”按钮并选择****检查****。 3. 控制台将打开，显示“添加到购物车”按钮的源代码。下图显示了控制台中突出显示的“添加到购物车”按钮的类。 ![控制台中的“添加到购物车”按钮代码，类等于 btn Product-form_cart-submit btn--secondary-accent 以黄色突出显示](https://klaviyo.zendesk.com/hc/article_attachments/28711672981275)
4. 将上例中突出显示的引号之间的按钮代码与上面代码片段中 `getElementsByClassName` 后面括号之间的内容进行比较。例如，屏幕截图中列出的类是“btn Product-form_cart-submit btn--secondary-accent”，代码段中列出的变量是“add-to-cart”。 5. 如果它们不匹配，请修改代码片段以匹配按钮的类。我们的示例的修改后的代码片段如下所示：
   ![Klaviyo 的备用“添加到购物车”代码段，其类名值 btn Product-form_cart-submit btn--secondary-accent](https://klaviyo.zendesk.com/hc/article_attachments/28711660835739)

如果您在尝试这些不同的选项后在跟踪“添加到购物车”时遇到问题，可能是由于识别“添加到购物车”按钮出现问题。 在这种情况下，[请联系 Klaviyo 支持人员。](https://help.klaviyo.com/hc/en-us/articles/115001002272-How-to-Contact-Support)

## 下一步：启用废弃的“添加到购物车”流程

默认的 Klaviyo 放弃购物车流程由 **结帐开始** 事件触发，而 **添加到购物车** 放弃购物车流程针对尚未开始结帐的更多休闲购物者。要启用此流程，我们建议使用 Klaviyo 流程库中提供的预构建流程：

1. 导航到 Klaviyo 的 [流库](https://www.klaviyo.com/library/flows)。 2. 单击进入“防止销售损失”目标部分。 3. 选择****添加到购物车触发器、放弃购物车提醒**** 流程。有两个选项：仅电子邮件，或电子邮件和短信。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28711673008667)
4. 如果您创建了 **添加到购物车** 事件，则此流程将准备好使用所有推荐的过滤器和动态电子邮件内容，以支持个性化购物车后续消息传递。 ## 您是否使用亚马逊 Prime 购买？如果您使用“Buy with Prime”来支持商店中任何产品的付款和配送，您应该：

- [将 Buy with Prime 与 Klaviyo 集成](https://help.klaviyo.com/hc/en-us/articles/14708088221467) 将 Buy with Prime 数据引入您的 Klaviyo 帐户。 - 对于已放弃的“添加到购物车”流程，请添加以下流程过滤器，以排除开始结账或通过“Buy with Prime”进行购买的客户收到错误消息：
  - **开始结帐**（使用 Prime 购买）**自开始此流程以来零次**并且
  - **下订单**（使用 Prime 购买）**自开始此流程以来零次。**

## 结果

您现在已创建并测试了 Shopify **添加到购物车** 事件，并启用了废弃的 **添加到购物车** 流程。 ## 其他资源

- [废弃购物车流程入门](https://help.klaviyo.com/hc/en-us/articles/115002779411-Guide-to-Creating-an-Abandoned-Cart-Flow)
- [Shopify 数据参考](https://help.klaviyo.com/hc/en-us/articles/115005080447-Reviewing-Your-Shopify-Data)
- [Shopify 集成问题排查](https://help.klaviyo.com/hc/en-us/articles/4403927899291-Troubleshooting-Your-Shopify-Integration)