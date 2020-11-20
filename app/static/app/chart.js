SIMPSONS={}
var cfg=[]
families.forEach(family => {
    if(family.father)cfg.push({type : 'node', id : 'family'+family.id.toString(), cls : 'fam', text : ' ', dataFullName : family.father.full_name})
    if(!family.father)cfg.push({type : 'node', id : 'family'+family.id.toString(), cls : 'fam', text : ' ', dataFullName : family.mother.full_name})
    
});
persons.forEach(person => {
    cfg.push({type : 'node', id : 'person'+person.id.toString(), text : person.first_name, dataFullName : person.full_name, style : { backgroundImage : SIMPSONS.marge }})
});

families.forEach(family => {
    if(family.father)cfg.push({type : 'link', source : 'family'+family.id.toString(), target : 'person'+family.father.id.toString()})
    if(family.mother)cfg.push({type : 'link', source : 'family'+family.id.toString(), target : 'person'+family.mother.id.toString()})
    family.childs.forEach(child => {
    cfg.push({type : 'link', source : 'family'+family.id.toString(), target : 'person'+child.id.toString()})
        
    });
});


var cdata = {
    type : 'tree',
    plotarea : {
        margin : 40
    },
    source : {
        align : 'left',
        text : 'Original idea by http://bmdata.co.uk/simpsons/'
    },
    options : {
        aspect : 'graph',
        springLength : 75,
        attractionConstant : 0.8,
        repulsionConstant : 4000,
        repulsionDistanceFactor : 20,
        node : {
            size : 24,
            borderWidth : 3,
            borderColor : '#036',
            backgroundColor : '#fff',
            backgroundRepeat : 'no-repeat',
            backgroundScale : 0.75,
            label : {
                color : '#000',
                fontWeight : 'bold',
                offsetY : 35
            },
            tooltip : {
                text : '%data-full-name'
            }
        },
        'node[cls-fam]' : {
            size : 12,
            borderWidth : 2,
            borderColor : '#000',
            backgroundColor : '#ccc',
            label : {
                visible : false
            }
        },
        link : {
            lineWidth : 2,
            lineColor : '#666'
        }
    },
    series : cfg
};

zingchart.render({
  id : 'myChart',
  width : '100%',
	height : '100%',
	output : 'canvas',
	data : cdata
});