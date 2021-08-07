// 0 -- with server synchro 
// 1 -- without server synchro -- only local
// const ipAPI = '//api.ipify.org?format=json'
let updateOPT = 1
const postUrl = "http://192.168.0.85:8000/majong_processor/name/"
const getUrl = "http://192.168.0.85:8000/majong_processor/name/"


const sloganList = [
  ' ╮( •́ω•̀ )╭ Ji~Ma~Jiang~',
  '芝麻酱...?',
  '计麻将啦～'
];

const addScoreBtn = document.getElementById('add-score');
const is1 = document.getElementById('is1');	
const is2 = document.getElementById('is2');	
const is3 = document.getElementById('is3');	
const is4 = document.getElementById('is4');

const p1 = document.getElementById('p-spring');	
const p2 = document.getElementById('p-summer');	
const p3 = document.getElementById('p-autumn');	
const p4 = document.getElementById('p-winter');

const l1 = document.getElementById('dong');	
const l2 = document.getElementById('nan');	
const l3 = document.getElementById('xi');	
const l4 = document.getElementById('bei');

const table = document.getElementById('table')
const JMJ = document.getElementById('JMJ')



const descform = document.getElementById('desc')
const syncform = document.getElementById('sync')
const scoreform = document.getElementById('score-form')
const clearform = document.getElementById('clear-form')
const resetform = document.getElementById('reset-form')
const playerdform =  document.getElementById('playerd');
const playernform =  document.getElementById('playern');
const playerxform =  document.getElementById('playerx');
const playerbform =  document.getElementById('playerb');

const balance1 = document.getElementById('set1')
const balance2 = document.getElementById('set2')
const balance3 = document.getElementById('set3')
const balance4 = document.getElementById('set4')

const plus1 = document.getElementById('s1win')
const plus2 = document.getElementById('s2win')
const plus3 = document.getElementById('s3win')
const plus4 = document.getElementById('s4win')

const minus1 = document.getElementById('s1lose')
const minus2 = document.getElementById('s2lose')
const minus3 = document.getElementById('s3lose')
const minus4 = document.getElementById('s4lose')

let roundID = 0
let tableRid = 0


const localStoragePlayers = JSON.parse(localStorage.getItem('Players'));
const localStorageScores = JSON.parse(localStorage.getItem('allScore'));
let allScore = localStorage.getItem('allScore') !== null ? localStorageScores : []; 
let Players = localStorage.getItem('Players') !== null ? localStoragePlayers : ['東方', '南宮', '西門', '北野']; 

//function definition
function init(){
  table.innerHTML = '';
  const ithr = document.createElement('th');
  const ith1 = document.createElement('th');
  const ith2 = document.createElement('th');
  const ith3 = document.createElement('th');
  const ith4 = document.createElement('th');
  const itr = document.createElement('tr')
  ithr.classList.add('round');
  ithr.innerHTML = 'R.';
  ith1.innerHTML = `${Players[0]}`;
  ith2.innerHTML = `${Players[1]}`;
  ith3.innerHTML = `${Players[2]}`;
  ith4.innerHTML = `${Players[3]}`;
  itr.appendChild(ithr);
  itr.appendChild(ith1);
  itr.appendChild(ith2);
  itr.appendChild(ith3);
  itr.appendChild(ith4);
  table.appendChild(itr);
  tableRid = 0;

  allScore.forEach(addScoreDOM);

  updateValues();

  switchSlogan();
}

function getSum(total, num) {
  // (acc, item) => (acc += item)
  return Number(total) + Number(num);
}

function updateValues(){
  const scorevalue =[
    allScore.map(oneRoundScore => oneRoundScore.is1),
    allScore.map(oneRoundScore => oneRoundScore.is2),
    allScore.map(oneRoundScore => oneRoundScore.is3),
    allScore.map(oneRoundScore => oneRoundScore.is4)];

  const total = [
    scorevalue[0].reduce(getSum, 0),
    scorevalue[1].reduce(getSum, 0),
    scorevalue[2].reduce(getSum, 0),
    scorevalue[3].reduce(getSum, 0)
  ];

  balance1.classList.remove(total[0]<0 ? 'plus':'minus');
  balance1.classList.add(total[0]<0 ? 'minus':'plus');

  balance2.classList.remove(total[1]<0 ? 'plus':'minus');
  balance2.classList.add(total[1]<0 ? 'minus':'plus');

  balance3.classList.remove(total[2]<0 ? 'plus':'minus');
  balance3.classList.add(total[2]<0 ? 'minus':'plus');

  balance4.classList.remove(total[3]<0 ? 'plus':'minus');
  balance4.classList.add(total[3]<0 ? 'minus':'plus');

  const plus = [
    scorevalue[0].filter(item => item > 0).reduce(getSum, 0),
    scorevalue[1].filter(item => item > 0).reduce(getSum, 0),
    scorevalue[2].filter(item => item > 0).reduce(getSum, 0),
    scorevalue[3].filter(item => item > 0).reduce(getSum, 0)
  ];

  const minus =[
    scorevalue[0].filter(item => item < 0).reduce(getSum, 0),
    scorevalue[1].filter(item => item < 0).reduce(getSum, 0),
    scorevalue[2].filter(item => item < 0).reduce(getSum, 0),
    scorevalue[3].filter(item => item < 0).reduce(getSum, 0)
  ];

  balance1.innerText = `${total[0]}`;
  balance2.innerText = `${total[1]}`;
  balance3.innerText = `${total[2]}`;
  balance4.innerText = `${total[3]}`;

  plus1.innerText = `+${plus[0]}`;
  plus2.innerText = `+${plus[1]}`;
  plus3.innerText = `+${plus[2]}`;
  plus4.innerText = `+${plus[3]}`;

  minus1.innerText = `${minus[0]}`;
  minus2.innerText = `${minus[1]}`;
  minus3.innerText = `${minus[2]}`;
  minus4.innerText = `${minus[3]}`;
}

// POST to & GET from server 
function updataData(){
  console.log(localStorage);
  if (updateOPT == 1) return;
  var ajax = new XMLHttpRequest();
  ajax.open('POST',postUrl, false);
  ajax.setRequestHeader("content-type","application/x-www-form-urlencoded");
  var info = JSON.stringify(localStorage);
  ajax.send(info);
  console.log(ajax.status);
  console.log(ajax.readyState);
  console.log(ajax.responseText);
  ajax.onreadystatechange=function(){
    if (ajax.readyState==4 && ajax.status==200){
      var result = ajax.responseText;
      if (result.status == "False"){
        alert("result -- False");
      }
    }
  }
  if(ajax.status == 200){
    var msg = ajax.responseText;
    console.log(msg);
  }else{alert("result -- False 2");}
}

function generateRoundID() {
  roundID += 1;
  return roundID;
}

function recordScore(sv, id,roundtr, pid){
  // Get sign 
  const sign = sv < 0 ? '-' : '+';
  //table method
  const playertd = document.createElement('td');
  // Add class based on value
  playertd.classList.add(sv < 0 ? 'minus' : 'plus');
  playertd.innerHTML = `${sign}${Math.abs(sv)}<button class="delete-btn  change" onclick="changeScore(${id}, ${pid})">✎</button>`;
  roundtr.appendChild(playertd)
}

function addScoreDOM(oneRoundScore) {
  // first add round list item
  tableRid += 1;
  const roundtd = document.createElement('td');
  const roundtr = document.createElement('tr')
  roundtd.classList.add('round')
  roundtd.innerHTML = `<button class="delete-btn" onclick="removeScore(${oneRoundScore.id})">x</button>${tableRid}`;
  roundtr.appendChild(roundtd)
  //then add score table item for each player
  recordScore(oneRoundScore.is1, tableRid, roundtr, 1);
  recordScore(oneRoundScore.is2, tableRid, roundtr, 2);
  recordScore(oneRoundScore.is3, tableRid, roundtr, 3);
  recordScore(oneRoundScore.is4, tableRid, roundtr, 4);
  // set for the table row color
  if(tableRid %2 ==0) roundtr.classList.add('cellcolor')
  table.appendChild(roundtr)
}

function removeScore(id) {
  allScore = allScore.filter(oneRoundScore => oneRoundScore.id !== id);

  updateLocalStorage();
}

function changeScore(r_id, pid){
  // ch_f.innerHTML= `  <input type="score" id="i4" > `;
  var x;
  
	var changeScore=prompt("请输入要修改的分数");
	if (changeScore!=''&changeScore!=null&!isNaN(changeScore)){    
    if(pid==1) allScore[r_id-1].is1 = changeScore;
    if(pid==2) allScore[r_id-1].is2 = changeScore;
    if(pid==3) allScore[r_id-1].is3 = changeScore;
    if(pid==4) allScore[r_id-1] .is4 = changeScore;
    updateLocalStorage();
    confirmChange();
	}
}

function confirmChange(){
  alert("已成功修改分数！")
}
// Update local storage allScore --> POST & GET
function updateLocalStorage() {
  localStorage.setItem('allScore', JSON.stringify(allScore));
  //console.log(Players)
  localStorage.setItem('Players', JSON.stringify(Players));

  init();

  updataData();
}

// Add one-round-Score
function addScore(e) {
  e.preventDefault();

  const oneRoundScore = {
    id: generateRoundID(),
    is1: isNaN(is1.value) ? 0 :is1.value, 
    is2: isNaN(is2.value) ? 0 :is2.value, 
    is3: isNaN(is3.value) ? 0 :is3.value, 
    is4: isNaN(is4.value) ? 0 :is4.value
  };

  allScore.push(oneRoundScore);

  updateLocalStorage();
  
  //init();  
}

function clearScore(){
  var r =  confirm("DO YOU WANT DELETE ALL SCORE RECORD?");
  if (r==true){
    // alert("ALL SCORE WILL BE DELETED！");
    allScore = [];
    localStorage.setItem('allScore', JSON.stringify(allScore));

    updateLocalStorage();

    roundID = 0;
	}
  
  
}

function resetlocalStorage(){
  var r =  confirm("DO YOU WANT RESET THE NAMES OF PLAYERS?");
  if (r==true){
    //localStorage.clear();
    Players = ['東方', '南宮', '西門', '北野'];
    //Players = ['spring', 'summer', 'autumn', 'winter'];
    localStorage.setItem('Players', JSON.stringify(Players));

    updateLocalStorage();

    clearScore();
	}
  
}

function setPlayer(e){
  e.preventDefault();
  Players = [
    p1.value!== '' ? p1.value : Players[0],
    p2.value!== '' ? p2.value : Players[1], 
    p3.value!== '' ? p3.value : Players[2], 
    p4.value!== '' ? p4.value : Players[3]
  ];

  l1.innerHTML = `${Players[0]}`;
  l2.innerHTML = `${Players[1]}`;
  l3.innerHTML = `${Players[2]}`;
  l4.innerHTML = `${Players[3]}`;

  

  localStorage.setItem('Players', JSON.stringify(Players));

  updateLocalStorage();

  updataData();
  p1.value = '';
  p2.value = '';
  p3.value = '';
  p4.value = '';

}

function syncScore(e){
  e.preventDefault();
  if (updateOPT == 1) return;
  var ajax = new XMLHttpRequest();
  ajax.open('GET',getUrl, false);
  ajax.setRequestHeader("content-type","application/x-www-form-urlencoded");
  ajax.send();
  console.log(ajax.status);
  console.log(ajax.readyState);
  console.log(ajax.responseText);
  ajax.onreadystatechange=function(){
    if (ajax.readyState==4 && ajax.status==200){
      var result = ajax.responseText;
      if (result.status == "False"){
        alert("result -- False");
      }
    }
  }
  if(ajax.status == 200){
    var msg = ajax.responseText;
    console.log(msg);
  }else{alert("result -- False 2");}

  localStorage = JSON.parse(result);

  init();
}

function switchSlogan(){
  //var slo = sloganList[ Math.floor((Math.random() * sloganList.length))];
  JMJ.innerHTML = `${sloganList[ Math.floor((Math.random() * sloganList.length))]}`
}

function description(){
  
  alert("这里是页面使用说明⊙ω⊙\n◔ω◔但其实也没什么可说明的。。。\nฅ点击页面右下角的喵爪试试ฅ");

}

init();

syncform.addEventListener('submit', syncScore); 

descform.addEventListener('click', description); 


scoreform.addEventListener('submit', addScore); 

resetform.addEventListener('submit', resetlocalStorage); 
clearform.addEventListener('submit', clearScore); 

playerdform.addEventListener('submit', setPlayer); 
playernform.addEventListener('submit', setPlayer); 
playerxform.addEventListener('submit', setPlayer); 
playerbform.addEventListener('submit', setPlayer); 


