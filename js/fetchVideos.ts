interface Video {
  title: string;
  views: number;
  likes: number;
}

let videos: Video[] = [
  {
    title: "",
    views: 0,
    likes: 0,
  },
];

const videosContainer = document.querySelector("#videos-container") as HTMLDivElement;
const videosErrorMessage = document.querySelector(
  "#videos-error-message"
) as HTMLParagraphElement;

const fetchVideos = async () => {
  try {
    const response = await fetch("http://127.0.0.1:5000/video/0", {
      method: "GET",
    });
    videos = await response.json();
    displayVideos();
  } catch (err: any) {
    console.log(err);
    videosErrorMessage.textContent = err.message;
  }
};
fetchVideos();

const displayVideos = () => {
  videos.forEach((video) => {
    const videoContainer = document.createElement("div");
    videoContainer.classList.add("video");

    const imageContainer = document.createElement("div");

    const videoImage = document.createElement("img");
    videoImage.src = "imgs/25481.jpg";
    imageContainer.appendChild(videoImage);

    const videoImageCredits = document.createElement("a");
    videoImageCredits.href = "https://www.freepik.com/vectors/video-screen";
    videoImageCredits.textContent =
      "Video screen vector created by starline - www.freepik.com";
    imageContainer.appendChild(videoImageCredits)

    videoContainer.appendChild(imageContainer);

    const detailsContainer = document.createElement("div");

    const videoTitle = document.createElement("p");
    videoTitle.innerHTML = `Title: <span style="color: red;">${video.title}</span>`;
    detailsContainer.appendChild(videoTitle);

    const videoViews = document.createElement("p");
    videoViews.innerHTML = `Views: <span style="color: yellow;">${video.views}</span>`;
    detailsContainer.appendChild(videoViews);

    const videoLikes = document.createElement("p");
    videoLikes.innerHTML = `Likes: <span style="color: yellow;">${video.likes}</span>`;
    detailsContainer.appendChild(videoLikes);

    videoContainer.appendChild(imageContainer);
    videoContainer.appendChild(detailsContainer);

    videosContainer.appendChild(videoContainer)
  });
};
