% rebase('layout.tpl', title=title, year=year)

<h2>{{ title }}.</h2>
<h3>This method will help you find a given fragment in a given graph</h3>

<p> </br> </p>
<h1> |------------------------------------------------------------------------------------------|</h1>
<h3> Instruction </h3>
<h3> This method can find a given fragment in a given graph. There are two fields, where you can put your graphs. First field is for main graph, 
second one is for fragment graph. You need to input matrix of your graphs in first and second fields. Below you can see the example of input, 
but this programm is smart and you can put your matrix any way you want, of course is matrix is correct </h3>
<img src = "static\images\ExamplePic1Method1.png ">
<h3> On this image you can see an example of matrixs</h3>
<p> </br> </p>
<h3> Arter inputing your graphs you need to press the button below and you will see a result</h3>
<img src = "static\images\ExamplePic2Method1.png ">
<h1> |------------------------------------------------------------------------------------------|</h1>
<p> </br> </p>

<form action="/method1" method="post">
    <h3> Input your graphs here </h3>
    <p><textarea rows="10" cols="45" name="graph1" placeholder = "Matrix of main graph"></textarea> <textarea rows="10" cols="45" name="graph2" placeholder = "Matrix of fragment graph"></textarea></p>
    <p><input type="submit" value="Find" name="find"></p> 

</form>

<p> </br> </p>

<p><a class="btn btn-default" href="/home">Back &raquo</a></p>