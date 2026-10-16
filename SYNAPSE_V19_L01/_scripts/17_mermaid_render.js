// Renderiza los diagramas Mermaid de informe/diagramas_mermaid.md a SVG (texto editable) y PNG en figuras/.
// Requiere playwright (chromium) y mermaid.min.js local: node 17_mermaid_render.js <ruta a mermaid.min.js>
const fs=require('fs'), path=require('path'); const {chromium}=require('/opt/node-tools/node_modules/playwright');
const L=path.join(__dirname,'..'); const md=fs.readFileSync(path.join(L,'informe','diagramas_mermaid.md'),'utf8');
const blocks=[...md.matchAll(/```mermaid\n([\s\S]*?)```/g)].map(m=>m[1]); const names=['fig_mermaid_flujo_proceso','fig_mermaid_relaciones_nucleo','fig_mermaid_valle_muerte'];
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'}).catch(()=>chromium.launch()); const pg=await b.newPage({deviceScaleFactor:2,viewport:{width:1400,height:900}});
 await pg.setContent('<html><body style="margin:0;background:#fff"><div id="g"></div></body></html>'); await pg.addScriptTag({path:process.argv[2]});
 await pg.evaluate(()=>mermaid.initialize({startOnLoad:false,theme:'neutral',flowchart:{htmlLabels:false,useMaxWidth:false},securityLevel:'loose'}));
 for(let i=0;i<blocks.length;i++){ const svg=await pg.evaluate(async(code)=>{const {svg}=await mermaid.render('d'+Math.random().toString(36).slice(2),code); document.getElementById('g').innerHTML=svg; return svg;},blocks[i]);
  // pasar a atributos los estilos calculados (Word y LibreOffice no aplican bien las hojas de estilo internas del SVG)
  const flat=await pg.evaluate(()=>{const svg=document.querySelector('#g svg'); const props=['fill','fill-opacity','stroke','stroke-width','stroke-dasharray','stroke-opacity','font-family','font-size','font-weight','text-anchor','opacity'];
    const els=[...svg.querySelectorAll('*')].filter(e=>e.tagName!=='style'); const vals=els.map(el=>{const cs=getComputedStyle(el); const o={}; props.forEach(p=>{const v=cs.getPropertyValue(p); if(v&&v!=='normal'&&!(p==='opacity'&&v==='1')) o[p]=v;}); return o;});
    els.forEach((el,i)=>{ Object.entries(vals[i]).forEach(([k,v])=>el.setAttribute(k,v)); el.removeAttribute('class'); el.removeAttribute('style'); });
    svg.querySelectorAll('style').forEach(e=>e.remove()); const w=svg.getBoundingClientRect(); svg.setAttribute('width',Math.round(w.width)); svg.setAttribute('height',Math.round(w.height)); return svg.outerHTML;});
  fs.writeFileSync(path.join(L,'figuras',names[i]+'.svg'),'<?xml version="1.0" encoding="UTF-8"?>\n'+flat); const el=await pg.$('#g svg'); await el.screenshot({path:path.join(L,'figuras',names[i]+'.png')}); console.log(names[i],svg.length); }
 await b.close();})();
