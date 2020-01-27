using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace WebApplication10.Models
{
    public class Device
    {

        public int DeviceId { get; set; }

        public string status { get; set; }

        public string automation { get; set; }

        public int ownerId { get; set; }
    }
}