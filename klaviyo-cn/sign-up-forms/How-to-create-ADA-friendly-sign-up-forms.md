---
id: "14980194112411"
title: "如何创建 ADA 友好的注册表单"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/14980194112411-How-to-create-ADA-friendly-sign-up-forms"
section: "Form best practices"
category: "Sign-up forms"
category_slug: "sign-up-forms"
klaviyo_updated: "2026-04-21T13:54:28Z"
language: "zh"
---
## 你将会学到

了解如何使用注册表单编辑器的 **表单警报** 选项卡中的辅助功能助理功能，以避免一些最常见的 Web 内容辅助功能指南 (WCAG) 合规性问题。努力使其网站符合 ADA 标准的公司应参考并遵循 WCAG 标准。辅助功能助理将指导您创建可供所有网站访问者访问的注册表单。 WCAG 标准旨在让所有人（包括残疾人）更容易访问网络内容。网站可访问性是许多国家/地区的法律要求，实施 WCAG 标准可以帮助满足许多此类可访问性需求。请注意，虽然辅助功能助手旨在帮助识别适用于注册表单的 WCAG 2.0 AA 标准下的辅助功能问题，但由于现有技术的已知限制或独立于技术的其他因素，它可能无法识别每个辅助功能要求。使用辅助功能助手可以帮助满足网络辅助功能要求，但不能保证遵守适用的法律。为了确认网络可访问性的法律含义和要求，建议寻求合格律师的建议。 ## 开始之前

以下是辅助功能助理将检查的问题列表。请注意，下面列出的错误类型是 Klaviyo 辅助功能助手识别它们的方式，而不是表单生成器中的特定输入字段名称。如果检测到错误，带有描述和修复提示的警报将出现在**表单警报**选项卡中。 |  |  |
| --- | --- |
| ****错误类型**** | ****描述**** |
|按钮名称 |确保按钮具有可识别的文本。 |
|图像替代|确保图像元素具有替代文本（alt text）或“none”的 html 角色或演示文稿。 |
|色彩对比|确保前景色和背景色之间的对比度符合 WCAG 2 AA 对比度阈值。 |
|文本块中的链接 |确保链接能够以不依赖颜色的方式与周围的文本区分开来。 |
|链接名称 |确保链接具有可识别的文本。 |
|标签|确保每个表单元素都有一个标签。 |

## 创建 ADA 友好的注册表单

无论您是构建第一个注册表单还是更新表单，辅助功能助手都可以帮助您识别和解决辅助功能问题。要创建符合上面列出的 WCAG 标准的表单：

1. 创建新的注册表单或打开现有注册表单之一的表单编辑器。 2. 使用编辑器[添加内容块](https://klaviyo.zendesk.com/hc/en-us/articles/4413550187035)并[设置表单样式](https://klaviyo.zendesk.com/hc/en-us/articles/4413537049883)以适合您的品牌。当您构建表单时，辅助功能助手将监控不符合 WCAG 标准的表单元素，并将其记录为**活动警报**。现有表单将在 **活动警报** 部分记录所有问题。 3. 单击左下角的****表单警报****，查看已识别的可访问性问题。在**活动警报**下，您将看到各种卡片，描述辅助功能助理在您的表单中识别出的不符合 WCAG 标准的元素，以及识别出的其他内容或设计问题。每张卡片都会包含问题的描述以及修复或消除问题的提示。例如，如果您将图像添加到注册表单中，辅助功能助手会提醒您将替代文本添加到图像中。替代文本提供图像的描述，以便使用屏幕阅读器浏览您网站的购物者可以访问数字内容。 ![注册表单编辑器左下角突出显示“表单警报”选项卡，并显示 2 个活动警报。](https://klaviyo.zendesk.com/hc/article_attachments/28717384388123)
   ![“表单警报”选项卡打开并显示在注册表单中发现的 3 个已识别的辅助功能问题。](https://klaviyo.zendesk.com/hc/article_attachments/28717384404123)
4. 要解决问题，请按照卡片上的建议进行操作，解决或添加缺失的元素。 对更改感到满意后，单击****修复********。**
   ![表单警报选项卡中的一个示例辅助功能问题，提示编辑块以解决该问题。](https://klaviyo.zendesk.com/hc/article_attachments/28717384405531)

   有些问题会提示您在相应块的设置（即按钮块）或样式部分中修复它们，而不是直接在 **表单警报** 选项卡中修复。要解决这些问题，请记下警报卡上的问题描述，然后单击****编辑块****（或****编辑样式****）以进行建议的更改。解决问题后，导航回****表单警报****选项卡。 5. 如果您希望忽略一项或多项辅助功能建议，请单击****关闭****。忽略问题将提示出现一个模式，要求您​​取消或确认您的选择。成功修复或消除所有已识别的问题后，您将在**表单警报**选项卡中看到“无活动警报”消息。 ![当您在 Gorm 警报选项卡中消除辅助功能问题时填充的消除警报模式。](https://klaviyo.zendesk.com/hc/article_attachments/28717390684827)
   ![表单警报选项卡中的切换开关允许您在活动警报和已解除警报之间切换。](https://klaviyo.zendesk.com/hc/article_attachments/28717390691227)

   您可以稍后通过打开助手并查看之前忽略的警报来返回忽略的问题。建议您修复辅助功能助手中突出显示的所有问题。不遵守 WCAG 标准可能会让您的公司面临法律风险。 6. 单击****发布****，在您的网站上设置包含辅助功能更新的注册表单。请注意，当您单击“发布”时，系统将提示您修复任何活动表单警报。您可以选择解决 **表单警报** 选项卡中的错误或仍然发布。 ## JAWS 可访问性报告

请注意，JAWS（适用于 Microsoft Windows 的计算机屏幕阅读器程序）可能无法检测您网站上在 Klaviyo 中创建的注册表单。为了确保使用 JAWS 的网站访问者仍然可以与您网站上的注册表单进行交互，我们建议向您的网站添加额外的代码片段，以便 JAWS 更容易访问该网站。复制以下代码片段并将其粘贴到您网站的主主题文件中，以便 JAWS 检测并读取您的 Klaviyo 注册表单：

````
  const isAriaHiddenTrue = ($el) => {
    常量 ariaHiddenValue = $el ? $el.getAttribute("aria-hidden") : null;
    返回 ariaHiddenValue === "true";
  };

  const isHTMLElement = (节点) => {
    返回node.nodeType === Node.ELEMENT_NODE;
  };

  const isModal = (节点) => {
    if (node.children.length !== 1) 返回 false;
    const modalContainer = Array.from(node.children[0].classList).some((cls) =>
      cls.startsWith("kl-private-reset")
    ）；

    返回模态容器；
  };

  const getTopLevelDomElements = () => {
    const body = document.body;

    // 使用children属性获取所有顶级元素
    const topLevelNodes = Array.from(body.children).filter((node) => {
      if (isHTMLElement(节点)) {
        const tagName = node.tagName.toLowerCase();

        console.log("isModal: ", isModal);

        // 过滤掉特定标签
        返回（
          标签名 !== "脚本" &&
          标签名 !== "链接" &&
          标签名 !== "iframe" &&
          标签名 !== "样式" &&
          !isModal(节点)
        ）；
      }
      返回假；
    });

    返回顶层节点；
  };

  const a11yHideTopLevelElements = () => {
    const $elements = getTopLevelDomElements();

    $elements.forEach(($el) => {
      if (!isAriaHiddenTrue($el)) {
        $el.setAttribute("kl-aria-hidden", "true");
        $el.setAttribute("aria-hidden", "true");
      }
    });
  };

  const a11yShowTopLevelElements = () => {
    const $elements = getTopLevelDomElements();

    $elements.forEach(($el) => {
      if ($el.hasAttribute("kl-aria-hidden")) {
        $el.removeAttribute("kl-aria-hidden");
        $el.removeAttribute("aria-hidden");
      }
    });
  };
````

## 后续步骤

在所有 Klaviyo 注册表中保持 WCAG 标准非常重要。之前发布的注册表单可能仍包含需要修复的辅助功能问题，但请注意，Klaviyo 不会自动修复任何 WCAG 不合规问题。 导航到编辑器中每个现有表单的 **表单警报** 选项卡，以解决任何可访问性问题，以帮助您的网站遵守 WCAG 合规性。