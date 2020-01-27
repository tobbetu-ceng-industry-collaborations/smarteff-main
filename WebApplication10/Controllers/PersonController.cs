using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using WebApplication10.Models;

namespace WebApplication10.Controllers
{
    public class PersonController : Controller


    {

        IList<Person> PersonList = new List<Person>()
        {new Person() { PersonId = 1, PersonName = "John", Age = 18 } ,
                            new Person() { PersonId = 2, PersonName = "Steve",  Age = 21 } ,
                            new Person() { PersonId = 3, PersonName = "Bill",  Age = 25 } ,
                            new Person() { PersonId = 4, PersonName = "Ram" , Age = 20 } , };
        // GET: Person
        public ActionResult Index()
        {
            var PersonList = new List<Person>{
                            new Person() { PersonId = 1, PersonName = "John", Age = 18 } ,
                            new Person() { PersonId = 2, PersonName = "Steve",  Age = 21 } ,
                            new Person() { PersonId = 3, PersonName = "Bill",  Age = 25 } ,
                            new Person() { PersonId = 4, PersonName = "Ram" , Age = 20 } ,
                             
                        };
            return View(PersonList);
        }

        [ActionName("find")]
        public ActionResult GetById(int id)
        {
            // get student from the database 
            return View();
        }


        public ActionResult Login(int Id)
        {
            //Get the student from studentList sample collection for demo purpose.
            //Get the student from the database in the real application
            var std = PersonList.Where(s => s.PersonId == Id).FirstOrDefault();

            return View(std);
        }
    }
}