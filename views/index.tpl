% rebase('layout.tpl', title='Home Page', year=year)

<div class="jumbotron">
    <img src = "static\images\logo_nav.png">
    <p></p>
    <p class="lead">Bottle is a free web framework for building great Web sites and Web applications using HTML, CSS and JavaScript.</p>
    <p><a href="http://bottlepy.org/docs/dev/index.html" class="btn btn-primary btn-large">Learn more &raquo;</a></p>
</div>

<div class="row">
    <div class="col-md-4">
        <h2>Getting started</h2>
        <p>
            Bottle gives you a powerful, patterns-based way to build dynamic websites that
            enables a clean separation of concerns.
        </p>
        <p><a class="btn btn-default" href="http://bottlepy.org/docs/dev/index.html">Learn more &raquo;</a></p>
    </div>
    <div class="col-md-4">
        <h2>Get more libraries</h2>
        <p>The Python Package Index is a repository of software for the Python programming language.</p>
        <p><a class="btn btn-default" href="https://pypi.python.org/pypi">Learn more &raquo;</a></p>
    </div>
    <div class="col-md-4">
        <h2>Microsoft Azure</h2>
        <p>You can easily publish to Microsoft Azure using Visual Studio. Find out how you can host your application using a free trial today.</p>
        <p><a class="btn btn-default" href="http://azure.microsoft.com">Learn more &raquo;</a></p>
    </div>
    <div class="col-md-4 offset-md-4">
        <h3> Ask a Question </h3>
        <form action="/home" method="post">
            <p><textarea rows="4" cols="50" name="QUEST" placeholder="Your question"></textarea></p> 
            <p><input type="text" size="50" name="NAME" placeholder="Your name"></p>
            <p><input type="text" size="50" name="ADRESS" placeholder="Your email"></p>
            <p><input type="date" name="DATE" placeholder="Date"></p>
            <p><input type="submit" value="Send" class="btn btn-default"></p>
        </form>
    </div>
    

</div>
