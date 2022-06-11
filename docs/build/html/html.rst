This is the template that renders the routes of the system. It uses bootstrap 5 and css for the UI  
This template inherits form from the input_form class. As a requirement, the form uses the secure random access to prevent from CSFR attack

This templates renders the 5 different buttons. Three of which are for easy navigation of modes. 
The forth button queries the database to output the the history of successfuly executed jobs
An action button sends the user input to the checker function to check if it is a valid job input


Different Messages in the category of success, error and information are flashed to the user depending on the activity of the user and the viability of the input job.






<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-0evHe/X+R7YkIZDRvuzKMRqM+OrBnVFBL6DOitfPri4tjfHxaWutUpFmBp4vmVor" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/js/bootstrap.bundle.min.js" integrity="sha384-pprn3073KE6tl6bjs2QrFaJGz5/SUsLqktiwsUTF55Jfv3qYSDhgCecCxMW52nD2" crossorigin="anonymous"></script>
    <link rel="stylesheet" href="static/index.css">
    <title>OQC</title>
</head>
<body >

    <div class="container-sm">
        <div class="row">
            <div class="col-8">
                <div>
                    <a class="active btn btn-lg btn-success m-3" href="#">Echo Mode</a>
                    <a class="btn btn-lg btn-outline-secondary m-3" href="#">Verbatim Mode</a>
                    <a class="btn btn-lg btn-outline-secondary m-3" href="#">Simulation Mode</a>

                    
                </div>

                <form method = "POST" action="/checker">
                    {{ form.hidden_tag() }}                 
        
                    <fieldset>
                        <div class="">
                            {% if form.inputString.errors %}
                                {{ form.inputString(class = "form-control form-control-lg border border-danger")}}
                                <div>
                                    {% for error in form.inputString.errors %}
                                        <span>{{error(class = "bg-danger")}}</span>
                                    {% endfor %}
                                </div>
                            {% else %}
                                {{ form.inputString(class = "form-control form-control-lg")}}
                            {% endif %}   
                        </div>
                    </fieldset>
                    <div>
                        {{form.submit(class = "btn btn-outline-info mt-5 mb-5")}}
                    </div>
        
                    {% with messages = get_flashed_messages(with_categories=true) %}
                        {% if messages %}
                            {% for category, message in messages %}
                                <div class="alert alert-{{category}}">
                                    {{message}}
                                </div>
                            {% endfor %}
                        {% endif%}
                    {% endwith %}
        
        
                </form>
            </div>

            <div class="col-4" >
                <div>
                    <form  action = "/get_history", method="GET">                        
                        <input class="btn btn-info btn-lg m-3 " type="Submit" value="History">
                    </form>
        
                    <div class="overflow-auto histories">
                        {% for history in histories %}

                            <h3>Job : {{history.input_string}}  </h3>
                            <h5>Report: {{history.result}}</h5>
                            <h5>Executed @: {{history.date}}</h5>
                            <hr>

                        {% endfor %}
                    </div>
                </div>
            </div>
        </div>
    </div>
</body>
</html>