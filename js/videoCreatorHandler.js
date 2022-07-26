import checkServerStatus from "./checkServerStatus.js";
let SERVER_STATUS = await checkServerStatus();
const videoCreatorContainer = document.querySelector("#video-creator-container");
const videoSendBtn = document.querySelector("#video-send-btn");
const videoErrorMessage = document.querySelector("#video-error-message");
const videoSuccessMessage = document.querySelector("#video-success-message");
videoSendBtn.addEventListener("click", async () => {
    if (SERVER_STATUS !== 200) {
        return (videoErrorMessage.textContent =
            "Couldn't connect to the server! Please, try refreshing the page");
    }
    videoErrorMessage.textContent = "";
    videoSuccessMessage.textContent = "";
    let newVideo = {};
    videoCreatorContainer.childNodes.forEach((child) => {
        const { value, id } = child;
        if (!value)
            return;
        newVideo = Object.assign(Object.assign({}, newVideo), { [id]: value });
    });
    try {
        const randomVideoId = Math.floor(Math.random() * 9999999);
        const response = await fetch(`http://127.0.0.1:5000/video/${randomVideoId}`, {
            method: "PUT",
            body: JSON.stringify(newVideo),
            headers: {
                "Content-type": "application/json; charset=UTF-8",
            },
        });
        const { message } = await response.json();
        if (response.status === 200) {
            return (videoSuccessMessage.textContent = message);
        }
        videoErrorMessage.textContent = `ERROR: ${message[Object.keys(message)[0]]}`;
    }
    catch (err) {
        console.log(err);
        videoErrorMessage.textContent = `ERROR: ${err.message}`;
    }
});
