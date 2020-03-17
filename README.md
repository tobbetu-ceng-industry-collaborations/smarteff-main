## ETU smarteff-main

This project is a smart office application which tracks devices, persons and shutdowns in an office environment. 

### Tech
The project uses a number of different technologies to work properly:

* [Flask]
* [Python]
* [SqLite]
* [SQLAlchemy]

### Installation

```sh
$ virtualenv -p $(which python3) env
$ source env/bin/activate
$ pip install -r requirements.txt
$ bash start.sh
```
After running the commands, you should be able to see the running demo on localhost in your preferred browser.

The default local server should be reachable on your machine via [127.0.0.1:5000](http://127.0.0.1:5000/admin).

The server should also be reachable inside the university network via [10.5.147.198:5000](http://10.5.147.198:5000/admin)

The server should also be reachable on [Heroku](https://smarteff.herokuapp.com/admin)

For more details, you can check out the logs of the application.

### Useful Links

[Admin Page](https://smarteff.herokuapp.com/admin)

[Person List](https://smarteff.herokuapp.com/ListPersons)

[Server Logs](https://smarteff.herokuapp.com/log)

### Team

[Deniz Güner](https://github.com/dguner)

[İpek Akova](https://github.com/ipekakova)

[Deniz Öner](https://github.com/denizonerr)

[Erhan Baturay Onural](https://github.com/BaturayOnural)

[Erhan Eker](https://github.com/erhanekerr)

[Caner Çoban](https://github.com/ccoban)

[Toygar Koca](https://github.com/ttoygarkoca)