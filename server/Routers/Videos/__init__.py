from flask_restful import Resource, reqparse, abort

video_put_args = reqparse.RequestParser()
video_put_args.add_argument(
    "title", type=str, help="The title of the video is required", required=True)
video_put_args.add_argument(
    "views", type=int, help="The amount of views of the video is required", required=True)
video_put_args.add_argument(
    "likes", type=str, help="The amount of likes on the video is required", required=True)

video_patch_args = reqparse.RequestParser()
video_patch_args.add_argument(
    "title", type=str, help="The title of the video")
video_patch_args.add_argument(
    "views", type=int, help="The amount of views of the video")
video_patch_args.add_argument(
    "likes", type=str, help="The amount of likes on the video")

videos = {}


def abortIfVideoDoesNotExist(videoId):
    if not videoId in videos:
        abort(404, message="Video not found...")


def abortIfVideoExists(videoId):
    if videoId in videos:
        abort(409, message="There's already a video with that ID...")


class Videos(Resource):
    def get(self, videoId):
        if(videoId == 0):
            returnedVideos = list()
            for video in videos.values():
                returnedVideos.append(video)
            return returnedVideos
        abortIfVideoDoesNotExist(videoId)
        return videos[videoId]

    def put(self, videoId):
        abortIfVideoExists(videoId)
        args = video_put_args.parse_args()
        videos[videoId] = args
        return {"message": "Video successfully added!"}

    def delete(self, videoId):
        abortIfVideoDoesNotExist(videoId)
        del videos[videoId]
        return '', 209

    def patch(self, videoId):
        abortIfVideoDoesNotExist(videoId)
        args = video_patch_args.parse_args()
        print(args)
        for k, v in args.items():
            if(v != None):
                videos[videoId][k] = v
        return {"message": "Video successfully patched!"}
