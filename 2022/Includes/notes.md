# Web

# Flag: picoCTF{1nclu51v17y_1of2_f7w_2of2_6edef411}

Can you get the flag? Go to this website and see what you can discover.

http://saturn.picoctf.net:59300/


```
On Includes

Many programming languages and other computer files have a directive, often called include (sometimes copy or import), that causes the contents of a second file to be inserted into the original file. These included files are called copybooks or header files. They are often used to define the physical layout of program data, pieces of procedural code and/or forward declarations while promoting encapsulation and the reuse of code.

Source: Wikipedia on Include directive 
[Button]On click it call a function from script.js
```

Look at the source

style.css
```
body {
  background-color: lightblue;
}

/*  picoCTF{1nclu51v17y_1of2_  */
```

script.js
```
function greetings()
{
  alert("This code is in a separate file!");
}

//  f7w_2of2_6edef411}
```
