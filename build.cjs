const fs = require('fs');
const path = require('path');
const esc = s => s.replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;');
const inline = s => esc(s).replace(/\*\*(.*?)\*\*/g,'<strong>$1</strong>').replace(/`(.*?)`/g,'<code>$1</code>');
function render(s) {
 const lines=s.trim().split(/\r?\n/); let out='', table=false, list=false;
 for(const line of lines){
  if(!line.startsWith('|')&&table){out+='</tbody></table>';table=false;}
  if(!line.startsWith('- ')&&list){out+='</ul>';list=false;}
  if(!line.trim())continue;
  if(line.startsWith('|')){if(/^\|[\s:|-]+\|$/.test(line))continue;const cells=line.split('|').slice(1,-1);if(!table){out+='<table><tbody>';table=true;}out+='<tr>'+cells.map(c=>'<td>'+inline(c.trim())+'</td>').join('')+'</tr>';}
  else if(line.startsWith('- ')){if(!list){out+='<ul>';list=true;}out+='<li>'+inline(line.slice(2))+'</li>';}
  else if(line.startsWith('## '))out+='<h2>'+inline(line.slice(3))+'</h2>';
  else if(line.startsWith('# '))out+='<h1>'+inline(line.slice(2))+'</h1>';
  else out+='<p>'+inline(line)+'</p>';
 }
 return out+(table?'</tbody></table>':'')+(list?'</ul>':'');
}
const pages=fs.readFileSync(path.join(__dirname,'PROPOSAL.md'),'utf8').split('<!-- PAGEBREAK -->');
fs.writeFileSync(path.join(__dirname,'PROPOSAL.html'),`<!doctype html><html lang="vi"><meta charset="utf-8"><title>PA1 — BakeOrder</title><style>
@page{size:A4;margin:12mm 14mm}*{box-sizing:border-box}body{font-family:Arial,sans-serif;color:#172335;margin:0;font-size:10pt;line-height:1.3}h1{font-size:18pt;margin:0 0 6px;color:#194d62}h2{font-size:11.5pt;margin:10px 0 5px;color:#194d62}p{margin:5px 0}ul{padding-left:17px;margin:5px 0}li{margin:3px 0}table{width:100%;border-collapse:collapse;font-size:9pt;line-height:1.22;margin:7px 0}td{border:1px solid #b7c5cc;padding:5px;vertical-align:top}tr:first-child{font-weight:bold;background:#eaf1f3}td:first-child{width:7%}td:nth-child(2){width:51%}td:nth-child(3){width:25%}td:nth-child(4){width:17%}code{font-size:9pt}.page{break-after:page}.page:last-child{break-after:auto}footer{font-size:8pt;color:#63717d;margin-top:9px;border-top:1px solid #d9e1e4;padding-top:4px}@media screen{body{background:#eee}.page{background:white;width:210mm;min-height:297mm;margin:15px auto;padding:12mm 14mm;box-shadow:0 2px 8px #bbb}}
</style>${pages.map((p,i)=>'<section class="page">'+render(p)+'<footer>BakeOrder · PA#1 · CSC13114 · Nhóm 23120225–23120226–23120229 · '+(i+1)+'/2</footer></section>').join('')}</html>`);
