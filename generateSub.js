const p5 = require('node-p5');

function sketch(p) {
    var particles = [] 
    var multiply;
    var circleSize;
    var espaçoEntreParticulas;
    var r;
    var g;
    var b;
    var backgroundAlpha;
    var loopValue;
    var toWait;
    let canva;
    var dimension;
    
    p.setup = () => {
        dimension = 800;
        canva = p.createCanvas(dimension , dimension);
        p.background(30);
		
		espaçoEntreParticulas = p.random(20, 60);
        for (var x = 0; x < dimension; x += espaçoEntreParticulas) {
			for (var y = 0; y < dimension; y += espaçoEntreParticulas) {
				var points = p.createVector(x, y);
                particles.push(points);
            }
        }
        
		circleSize = p.random(1, 10)

		r = p.random(0, 255);
		g = p.random(0, 255);
		b = p.random(0, 255);
		backgroundAlpha = p.random(0, 20)

		multiply = p.random(0.001, 0.006);

        toWait = p.random(75, 125)
        loopValue = 0;

		p.fill(r, g, b);
    }
    
    p.draw = () => {
        p.noStroke()
        p.background(30, backgroundAlpha)
        var radius = dimension/2

        for(var i = 0; i < particles.length; i++){
			var x = particles[i].x, y = particles[i].y;
			var angle = p.noise(x * multiply, y * multiply) * 360;
            particles[i].add(p.createVector(p.cos(angle), p.sin(angle)));

            var alpha = p.map(p.dist(radius, radius, x, y), 0, radius, radius, 0)
			p.fill(r, g, b, alpha)
    
            if(p.dist(radius, radius, x, y) < radius){
                p.ellipse(x, y, circleSize); 
            }else{
                particles[i].x = p.random(dimension);
                particles[i].y = p.random(dimension);
            }
        }

        if(loopValue >= toWait){
			p.fill(r,g,b);
			p.stroke(30, 240);
			p.strokeWeight(20);
			p.textAlign(p.CENTER, p.CENTER);
			p.textSize(120);
			p.text('Subscribe', dimension / 2, dimension / 2);
            p.noLoop();
            p.saveCanvas(canva, 'images/subscribe/sub', 'png');
            console.log('New img gerated!');
            return
        }

        loopValue += 1;
    }
}

let p5Instance = p5.createSketch(sketch);
// module.exports = p5Instance
