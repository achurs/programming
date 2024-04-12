import './App.css'
import './custom.css'
import { useState } from 'react'
import './daily-refesh.js'
function setCookie(name,value) {
  const time = 2147483647;
  document.cookie = name + "=" + value + ";max-age=" + time;
}
function getCookie(name) {
  const cDecoded = decodeURIComponent(document.cookie);
  const cArray = cDecoded.split('; ');
  let res = "";
  cArray.forEach((element) => {
    const c = element.split("=");
    if (c[0] === name) {
      console.log(c[1])
      res = c[1];
    }
  })
  return res;
  }
function daycounter(date1, date2) {
  const diffTime = Math.abs(date2 - date1);
  const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
  return diffDays
  
}
function App() {
  let temp = getCookie("date");
  if (temp === "") {
    temp = new Date().toJSON().slice(0,10);
  }
  const [date, setDate] = useState(temp);
  let currentdate = new Date();
  const [days, setDays] = useState(daycounter(new Date(date), currentdate));
  return (
    <>
    <h1>Day Counter</h1>
    <div>
    <input type="date" placeholder='enter date' id='date-inputer' />
    <button id='date-button' onClick={() => {
      setDate(document.getElementById('date-inputer').value)
      setCookie("date", document.getElementById('date-inputer').value)
      setDays(daycounter(new Date(date), currentdate))
    }}>Click</button>
    </div>
    {date}
    <h1>{days} days</h1>
    </>
  )
}

export default App
