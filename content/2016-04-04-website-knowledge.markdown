Title: Basic Web Knowledge
Date: 2016-04-04 23:28
Modified: 2017-01-16 13:45
Category: Web-Dev
Tags: DOM,Web-Dev,browsers,WebComponents
Slug: basic-web-know
Authors: Rishabh Chakrabarti
Summary: Basic Web Knowledge and points about DOM, Web Components, Shadow DOM etc.


## Basic Web Knowledge

# What is the Document Object Model?

The Document Object Model is a platform- and language-neutral interface that will allow programs and scripts to dynamically access and update the content,
structure and style of documents. The document can be further processed and the results of that processing can be incorporated back into the presented page.

It provides a structured representation of the [document as a tree](https://www.w3.org/TR/DOM-Level-1/introduction.html).
The DOM defines methods that allow access to the tree, so that they can change the document structure, style and content. The DOM provides a representation of the document as a structured group of nodes and objects, possessing various properties and methods.
Nodes can also have event handlers attached to them, and once an event is triggered, the event handlers get executed. Essentially, it connects web pages to scripts or programming languages.

# Why the Document Object Model?

"Dynamic HTML" is a term used by some vendors to describe the combination of HTML, style sheets and scripts that allows documents to be animated.
The W3C has received several submissions from members companies on the way in which the object model of HTML documents should be exposed to scripts.
These submissions do not propose any new HTML tags or style sheet technology

# $hadow DOM 101

When making widgets out of HTML5 and Javascript, the DOM tree inside a widget isn't encapsulated.  
The lack of encapsulation means your document stylesheet might accidentally apply to parts inside the widget.  
* Your JS might accidentally modify parts inside the widget.
* IDs may overlap with IDs inside the widget.
* Upgrading might break the widget's internal details

# WebComponents
1. Templates
2. Shadow DOM
3. Custom Elements
4. Packaging

Shadow DOM addresses the DOM encapsulation problem.  
## Shadow World

With Shadow DOM, elements can get a new kind of node associated with them.  
This new kind of node is called **shadow root**. The element that has a shadow root associated with it is called a **shadow host**.  

We need to create a Shadow Root for the element -> #nameTag.

```javascript
<script>
var shadow = document.querySelector('#nameTag').createShadowRoot();
var template = document.querySelector('#nameTagTemplate');
var clone = document.importNode(template.content, true);
shadow.appendChild(clone);
</script>
```

Using the Shadow DOM, we have hidden the presentation details from the actual DOM.

## REST :
