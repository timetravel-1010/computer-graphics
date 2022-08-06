var scene = new THREE.Scene();
var camera = new THREE.PerspectiveCamera( 75, window.innerWidth/window.innerHeight, 0.1, 1000 );

var renderer = new THREE.WebGLRenderer();
renderer.setSize( window.innerWidth, window.innerHeight );
document.body.appendChild( renderer.domElement );

camera.position.z = 10;

var controls = new THREE.OrbitControls(camera, renderer.domElement);
controls.enableDamping = true;
controls.campingFactor = 0.25
controls.enableZoom = true;

var keyLight = new THREE.DirectionalLight(new THREE.Color('hsl(30, 100%, 75%)'), 1.0);
//keyLight.position.set(-100, 0, 100);
keyLight.position.set(-10, 10, 10);

var fillLight = new THREE.DirectionalLight(new THREE.Color('hsl(240, 100%, 75%)'), 0.75);
//fillLight.position.set(100, 0, 100);
fillLight.position.set(10, 0, 10);

var backLight = new THREE.DirectionalLight(0xffffff, 1.0);
//backLight.position.set(100, 0, -100).normalize();
backLight.position.set(10, 0, -10).normalize();

scene.add(keyLight);
scene.add(fillLight);
scene.add(backLight);

var mtlLoader = new THREE.MTLLoader();
mtlLoader.setTexturePath('/assets/');
mtlLoader.setPath('/assets/');
mtlLoader.load('sunny-park.mtl', function(materials) {
	materials.preload();
	var objLoader = new THREE.OBJLoader();
	objLoader.setMaterials(materials);
	objLoader.setPath('/assets/');
	objLoader.load('sunny-park.obj', function(object){
		object.position.y -= 0;
		scene.add(object);
	});
});



var animate = function () {
	requestAnimationFrame( animate );

	controls.update();

	renderer.render(scene, camera);
};

animate();