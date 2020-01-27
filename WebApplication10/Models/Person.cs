using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace WebApplication10.Models
{
    public class Person
    {

        public int PersonId { get; set; }
        public string PersonName { get; set; }
        public int Age { get; set; }

        public Device Device { get; set; }

    }
}