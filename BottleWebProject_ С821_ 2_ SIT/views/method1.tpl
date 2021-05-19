% rebase('layout.tpl', title=title, year=year)

<h2>{{ title }}.</h2>
<h3>This method will find a given fragment in a given graph</h3>

<p> </br> </p>

<form action="/method1" method="post">
    <h3> Input your graphs here </h3>
    <p><textarea rows="10" cols="45" name="graph1"></textarea> <textarea rows="10" cols="45" name="graph2"></textarea></p>
    <p><input type="submit" value="Find" name="find"></p> 
</form>

<p> </br> </p>

<p><a class="btn btn-default" href="/home">Back &raquo</a></p>