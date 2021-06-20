const images = ["0.jpeg", "1.jpeg", "2.jpeg", "3.jpg", "4.jpg"];

const chosenImage = images[Math.floor(Math.random() * images.length)];

const bgImg = document.createElement("img");
bgImg.src = `Img/${chosenImage}`;
document.body.appendChild(bgImg);
