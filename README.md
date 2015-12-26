![travisCI](https://travis-ci.org/brennan-v-/flaskr-neo4j.svg) [![Codecov](https://img.shields.io/codecov/c/github/brennan-v-/flaskr-neo4j.svg)](https://codecov.io/github/brennan-v-/flaskr-neo4j?branch=master)
 ![python](https://img.shields.io/badge/python-2.7%2C%203.3%2C%203.4%2C%203.5%2C%203.5--dev-blue.svg) ![neo4j](https://img.shields.io/badge/neo4j-2.0.4%2C%202.1.8-blue.svg)

                         / flaskr-neo4j /

                 a minimal blog application


    ~ What is flaskr-neo4j?

      A neo4j powered thumble blog application

    ~ How do I use it?

      1. install and start neo4j from http://neo4j.com

      2. clone the repo and step into it

          git clone git@github.com:brennan-v-/flaskr-neo4j.git
          cd flaskr-neo4j

      3. create a virtual environment and install packages

          virtualenv venv
          source venv/bin/activate

          pip install -r requirements.txt

            or
            
          pip install flask
          pip install py2neo

      4. start the application

          python flaskr.py

         the application will greet you on
         http://localhost:5000/

    ~ Attributions:

[mitsuhiko/flask/examples/flaskr](https://github.com/mitsuhiko/flask/tree/master/examples/flaskr/) [![GitHub stars](https://img.shields.io/github/stars/mitsuhiko/flask.svg?style=social&label=Star)](https://github.com/mitsuhiko/flask)

[neo4j/neo4j](https://github.com/neo4j/neo4j) [![GitHub stars](https://img.shields.io/github/stars/neo4j/neo4j.svg?style=social&label=Star)](https://github.com/neo4j/neo4j)

[nigelsmall/py2neo](https://github.com/nigelsmall/py2neo) [![GitHub stars](https://img.shields.io/github/stars/nigelsmall/py2neo.svg?style=social&label=Star)](https://github.com/nigelsmall/py2neo)

[nicolewhite/neo4j-flask](https://github.com/nicolewhite/neo4j-flask) [![GitHub stars](https://img.shields.io/github/stars/nicolewhite/neo4j-flask.svg?style=social&label=Star)](https://github.com/nicolewhite/neo4j-flask)
