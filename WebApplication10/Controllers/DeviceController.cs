using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using WebApplication10.Models;

namespace WebApplication10.Controllers
{
    public class DeviceController : Controller
    {
        // GET: Device
        IList<Device> DeviceList = new List<Device>()
        {new Device() { DeviceId = 11, status = "on", automation = "on",ownerId=2 } ,
                            new Device() { DeviceId = 21, status = "off",  automation = "on", ownerId=1 } ,
                            new Device() { DeviceId = 31, status = "on",  automation = "off", ownerId=2  } ,
                            new Device() { DeviceId = 41, status = "on" , automation = "on" ,ownerId=1 } , };
        public ActionResult Index()
        {
            return View();
        }

        public ActionResult devicereturn(int Id)
        {
            //Get the student from studentList sample collection for demo purpose.
            //Get the student from the database in the real application
            var std = DeviceList.Where(s => s.ownerId == Id).FirstOrDefault();

            return View(std);
        }
    }
}