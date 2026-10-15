// Genera el DOCX en formato APA 7 a partir de documento/bloques.json
const fs=require('fs'); const path=require('path');
const {Document,Packer,Paragraph,TextRun,Table,TableRow,TableCell,WidthType,AlignmentType,BorderStyle,Header,PageNumber,LevelFormat,ShadingType,PageBreak,TabStopType,ImageRun}=require('docx');
const D=JSON.parse(fs.readFileSync(path.join(__dirname,'../documento/bloques.json'),'utf8'));
const FONT='Times New Roman', SZ=24, DOUBLE=480, W_PAGE=12240, MARG=1440, W_TXT=W_PAGE-2*MARG;
function runs(text,base={}){ // **negrita**, *cursiva*
  const out=[]; const re=/(\*\*[^*]+\*\*|\*[^*]+\*)/g; let last=0,m;
  text=String(text);
  while((m=re.exec(text))){ if(m.index>last) out.push(new TextRun({text:text.slice(last,m.index),font:FONT,size:base.size||SZ,...base}));
    const t=m[0]; if(t.startsWith('**')) out.push(new TextRun({text:t.slice(2,-2),bold:true,font:FONT,size:base.size||SZ,...base})); else out.push(new TextRun({text:t.slice(1,-1),italics:true,font:FONT,size:base.size||SZ,...base}));
    last=m.index+t.length; }
  if(last<text.length) out.push(new TextRun({text:text.slice(last),font:FONT,size:base.size||SZ,...base}));
  return out; }
const CS=20;
const body=(t,o={})=>new Paragraph({children:runs(t),spacing:{line:DOUBLE,before:0,after:0},indent:{firstLine:720},...o});
const kids=[];
// ---- Portada
const sp=(n)=>{for(let i=0;i<n;i++) kids.push(new Paragraph({children:[new TextRun({text:'',font:FONT,size:SZ})],spacing:{line:DOUBLE}}));};
sp(3);
kids.push(new Paragraph({alignment:AlignmentType.CENTER,spacing:{line:DOUBLE},children:[new TextRun({text:D.meta.titulo,bold:true,font:FONT,size:SZ})]}));
sp(1);
for(const t of ['SYNAPSE V19.0 (análisis asistido por inteligencia artificial)','Preparado para: Andrés Calderón','Lote L01 del repositorio TejidoEmpresarial','15 de octubre de 2026'])
  kids.push(new Paragraph({alignment:AlignmentType.CENTER,spacing:{line:DOUBLE},children:[new TextRun({text:t,font:FONT,size:SZ})]}));
kids.push(new Paragraph({children:[new PageBreak()]}));
// ---- Resumen
kids.push(new Paragraph({alignment:AlignmentType.CENTER,spacing:{line:DOUBLE},children:[new TextRun({text:'Resumen',bold:true,font:FONT,size:SZ})]}));
kids.push(new Paragraph({spacing:{line:DOUBLE},children:runs(D.meta.resumen)}));
kids.push(new Paragraph({spacing:{line:DOUBLE},indent:{firstLine:720},children:[new TextRun({text:'Palabras clave: ',italics:true,font:FONT,size:SZ}),new TextRun({text:D.meta.kw,font:FONT,size:SZ})]}));
kids.push(new Paragraph({children:[new PageBreak()]}));
// título repetido (inicio del texto)
kids.push(new Paragraph({alignment:AlignmentType.CENTER,spacing:{line:DOUBLE},children:[new TextRun({text:D.meta.titulo,bold:true,font:FONT,size:SZ})]}));
// ---- Tablas
const bT={style:BorderStyle.SINGLE,size:8,color:'000000'}, bN={style:BorderStyle.NONE,size:0,color:'FFFFFF'};
let tabN=0;
function table(b){
  if(!b.c) tabN++; const nc=Math.max(...b.rows.map(r=>r.length)); const rows=b.rows.map(r=>r.concat(Array(nc-r.length).fill('')));
  let w=b.w; if(!w){ const mx=Array(nc).fill(1); rows.forEach(r=>r.forEach((c,i)=>{mx[i]=Math.max(mx[i],Math.min(String(c).length,60));})); const s=mx.reduce((a,c)=>a+c,0); w=mx.map(v=>Math.max(8,Math.round(100*v/s))); const t=w.reduce((a,c)=>a+c,0); w=w.map(v=>Math.round(100*v/t)); }
  const tot=w.reduce((a,c)=>a+c,0); const cw=w.map(v=>Math.floor(W_TXT*v/tot)); cw[cw.length-1]+=W_TXT-cw.reduce((a,c)=>a+c,0);
  const sz=b.c?16:(b.small?18:20);
  const out=[];
  if(!b.c) out.push(new Paragraph({keepNext:true,spacing:{line:DOUBLE>>1+240,before:120,after:0},children:[new TextRun({text:'Tabla '+tabN,bold:true,font:FONT,size:SZ})]}));
  if(!b.c) out.push(new Paragraph({keepNext:true,spacing:{line:240,after:120},children:[new TextRun({text:(b.cap?b.cap[0]:'')+(b.cap&&b.cap[1]?': '+b.cap[1]:''),italics:true,font:FONT,size:SZ})]}));
  const tr=rows.map((r,ri)=>new TableRow({tableHeader:ri===0,cantSplit:true,children:r.map((c,ci)=>new TableCell({width:{size:cw[ci],type:WidthType.DXA},margins:{top:40,bottom:40,left:80,right:80},
    borders:{top:ri===0?bT:bN,bottom:(ri===0||ri===rows.length-1)?bT:bN,left:bN,right:bN},
    children:[new Paragraph({spacing:{line:240},children:runs(c,{size:sz,bold:ri===0})})]}))}));
  out.push(new Table({width:{size:W_TXT,type:WidthType.DXA},columnWidths:cw,rows:tr}));
  out.push(new Paragraph({spacing:{line:240,after:200},children:[new TextRun({text:'',font:FONT,size:sz})]}));
  return out; }
// ---- Bloques
const numRefs=[]; let olCount=0;
for(const b of D.blocks){
  if(b.t==='h1') kids.push(new Paragraph({alignment:AlignmentType.CENTER,keepNext:true,spacing:{line:DOUBLE},children:runs(b.x,{bold:true})}));
  else if(b.t==='h2') kids.push(new Paragraph({keepNext:true,spacing:{line:DOUBLE},children:runs(b.x,{bold:true})}));
  else if(b.t==='h3') kids.push(new Paragraph({keepNext:true,spacing:{line:DOUBLE},children:runs(b.x,{bold:true,italics:true})}));
  else if(b.t==='fh1') kids.push(new Paragraph({pageBreakBefore:true,keepNext:true,spacing:{line:260,after:120},children:runs(b.x,{bold:true,size:24})}));
  else if(b.t==='fh2') kids.push(new Paragraph({keepNext:true,spacing:{line:260,before:160,after:80},children:runs(b.x,{bold:true,size:22})}));
  else if(b.t==='fh3'||b.t==='fh4') kids.push(new Paragraph({keepNext:true,spacing:{line:260,before:120,after:60},children:runs(b.x,{bold:true,italics:true,size:CS})}));
  else if(b.t==='fig'){
    const fs=require('fs'), path=require('path'); const fp=path.join(__dirname,'..','figuras',b.f); const buf=fs.readFileSync(fp);
    const w0=buf.readUInt32BE(16), h0=buf.readUInt32BE(20); const maxW=6.5*96, maxH=7.4*96; const sc=Math.min(maxW/w0,maxH/h0); const w=Math.round(w0*sc), h=Math.round(h0*sc);
    kids.push(new Paragraph({keepNext:true,spacing:{line:DOUBLE,before:120},children:[new TextRun({text:'Figura '+b.num,bold:true,font:FONT,size:SZ})]}));
    kids.push(new Paragraph({keepNext:true,spacing:{line:240,after:120},children:[new TextRun({text:b.x,italics:true,font:FONT,size:SZ})]}));
    kids.push(new Paragraph({keepNext:true,alignment:AlignmentType.CENTER,spacing:{line:240,after:80},children:[new ImageRun({type:'png',data:buf,transformation:{width:w,height:h},altText:{title:b.x,description:b.x,name:b.f}})]}));
    kids.push(new Paragraph({spacing:{line:240,after:240},children:runs(b.n,{size:20})}));
  }
  else if(b.t==='p'&&b.c) kids.push(new Paragraph({spacing:{line:240,after:80},children:runs(b.x,{size:CS})}));
  else if(b.t==='p') kids.push(body(b.x));
  else if(b.t==='ul') b.items.forEach(x=>kids.push(new Paragraph({numbering:{reference:'bul',level:0},spacing:{line:b.c?240:DOUBLE,after:b.c?60:0},children:runs(x,b.c?{size:CS}:{})})));
  else if(b.t==='ol'){ olCount++; b.items.forEach(x=>kids.push(new Paragraph({numbering:{reference:'ol'+olCount,level:0},spacing:{line:b.c?240:DOUBLE,after:b.c?60:0},children:runs(x,b.c?{size:CS}:{})}))); numRefs.push('ol'+olCount); }
  else if(b.t==='ref') kids.push(new Paragraph({spacing:{line:DOUBLE},indent:{left:720,hanging:720},children:runs(b.x)}));
  else if(b.t==='pb') kids.push(new Paragraph({children:[new PageBreak()]}));
  else if(b.t==='table') table(b).forEach(x=>kids.push(x));
}
const numbering={config:[{reference:'bul',levels:[{level:0,format:LevelFormat.BULLET,text:'•',alignment:AlignmentType.LEFT,style:{paragraph:{indent:{left:720,hanging:360}}}}]},
  ...numRefs.map(r=>({reference:r,levels:[{level:0,format:LevelFormat.DECIMAL,text:'%1.',alignment:AlignmentType.LEFT,style:{paragraph:{indent:{left:720,hanging:360}}}}]}))]};
const doc=new Document({creator:'SYNAPSE V19.0',title:D.meta.titulo,styles:{default:{document:{run:{font:FONT,size:SZ}}}},numbering,
  sections:[{properties:{page:{size:{width:12240,height:15840},margin:{top:MARG,bottom:MARG,left:MARG,right:MARG}}},
    headers:{default:new Header({children:[new Paragraph({alignment:AlignmentType.RIGHT,children:[new TextRun({children:[PageNumber.CURRENT],font:FONT,size:SZ})]})]})},children:kids}]});
Packer.toBuffer(doc).then(b=>{fs.writeFileSync(path.join(__dirname,'../documento/Informe_Lote_L01_SYNAPSE_APA7.docx'),b);console.log('docx escrito',b.length)});
