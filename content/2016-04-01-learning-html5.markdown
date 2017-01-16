---
layout: post
title:  "Learning HTML5"
date:   2016-03-29 17:11:43 +0530
categories: learning
tags:
- learning

---

## HTML5 it is...
This blog contains the notes and results of my experiments with HTML5. Through this blog, I also plan to learn [Markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) so it's a multi-purpose blog.   
I am basically experimenting with Polymer and I demand to swim through code and simply dive-in **i.e. learn as I code.**

# [Polyglot Markup](https://en.wikipedia.org/wiki/Polyglot_markup)

A Polyglot is basically someone who can speak several languages.   
But in HTML5, Polyglot means something else... It's basically a document or script written in a valid form of multiple markup languages, which performs the same output independent of the markup's parser, layout engine or interpreter.  
Polyglot HTML is HTML that has been written to conform to both HTML and XHTML specifications.
Therefore, a polyglot document can be parsed as either HTML or XML, and will produce the same [DOM](https://en.wikipedia.org/wiki/Document_Object_Model) structure either way.

For an HTML5 document to meet these criteria, the 2 requirements are that:  


* It must have an HTML5 doctype,
* Be written in well-formed XHTML.

# What is XHTML?
XHTML is a variant of HTML that uses the syntax of XML, the Extensible Markup Language. XHTML has all the same elements (for paragraphs, etc.) as the HTML variant, but the syntax is slightly different. Because XHTML is an XML application, you can use other XML tools with it (such as XSLT, a language for transforming XML content).

# DOCTYPE
A DOCTYPE or Document Type Declaration originates from HTML's SGML lineage. It's use is for legacy purpose only.  
It was originally used to refer to a Document Type Definition (DTD) — a formal declaration of the elements, attributes and syntactic features that could be used within the document.  
In HTML5, there are three modes :


* Quirks mode,
* Limited quirks mode
* No quirks mode

Only **No quirks mode** is conforming to use. In each of these three modes, there are some differences in the way the documents are visually rendered.  
To ensure the most standards compliant rendering, it is important to ensure the **No quirks mode** is used.  
Thus, the DOCTYPE in the new definition, defines the no-quirks mode in browsers. 

# Elements 

There are 5 different types of elements:


1. Normal - `<Start tag> Content <End tag>` 
2. Void - Empty elements, i.e. forbidden from containing any content at all. The self-closing tag syntax is used. 
  * E.g. `<hr/>`
3. Raw text - `<Start tag> Content <End tag>`
  * Here, the content is treated as raw text instead of markup. E.g. `<script>`.  
  In the script tags, escape sequences are needed too if there's a clash. 
4. RCDATA - The term RCDATA elements refers to elements within which character references are supported, but all other content is treated as raw text instead of markup.  
  * `<Start tag> Content <End Tag>`.E.g. `<textarea>` Character references like `&amp;` are valid. 
5. Foreign Elements - Elements in SVG and MathML namespaces.

### Empty Attribute syntax

An empty attribute is one where the value has been omitted. This is syntactic shorthand for specifying the attribute with an empty value, and is *commonly used for boolean attributes*.
E.g. `<input disabled>` . Here, `disabled` is a boolean attribute.

### Unquoted Attribute Syntax

Attribute where the value is supplied but is not surrounded by quotation marks.  
E.g. `<img src = image.png>`

## HTML Vocabulary and APIs


1. Metadata content
  Metadata content includes elements for marking up document metadata;
  marking up or linking to resources that describe the behaviour or presentation of the document; or indicate relationships with other documents. 
  
  '<head>, <title>, <meta>, <link>, <script>, <style>`

* Flow content

* Sectioning root
* Sectioning content
* Heading content
* Phrasing content
* Embedded content
* Interactive content
* Transparent
