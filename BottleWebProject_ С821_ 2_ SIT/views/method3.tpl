% rebase('layout.tpl', title=title, year=year)

<h2>{{ title }}.</h2>
<h3>Finding an Euler cycle in graph.</h3>
<h3>This method searches for an Euler cycle. This cycle should go through all the ribs once.
This method works with matrices of any dimension.</h3>

<h4> Matrix:  </h4>
<form action="/method3" method="post">
        <p><textarea rows="10" cols="45" name="matrix"  placeholder="Type matrix there"></textarea></p>
        <p><input type="submit" value="Find" name="button"</p>
</form>

<p><a class="btn btn-default" href="/home">Back &raquo</a></p>