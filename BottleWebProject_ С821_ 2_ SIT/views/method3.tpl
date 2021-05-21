% rebase('layout.tpl', title=title, year=year)

<h2>{{ title }}.</h2>
<p>Finding an Euler cycle in graph.</p>
<p>This method searches for an Euler cycle. This cycle should go through all the ribs once.
This method works with matrices of any dimension.</p>
<img src = "static\images\graph.png"
<br>
<p>Example:</p>
<img src = "static\images\example.png"
<br>
<p> Matrix:  </p>
<form action="/method3" method="post">
        <p><textarea rows="10" cols="45" name="matrix"  placeholder="Type matrix there"></textarea></p>
        <p><input type="submit" value="Find" name="button"</p>
</form>

<p><a class="btn btn-default" href="/home">Back &raquo</a></p>