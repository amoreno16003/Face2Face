const APP_ID = '74db7ea6b53941d5aba1c335903798da'
const CHANNEL = 'main'
const TOKEN = '007eJxTYHCKXNWzhHdyg9S0CVNPyjOHljZ8PHpSPzB+4wXObqenl9oUGMxNUpLMUxPNkkyNLU0MU0wTkxINk42NTS0NjM0tLVIST0fOTG4IZGTYUjyBiZEBAkF8FobcxMw8BgYAR1EfvQ=='
let UID;

const client = AgoraRTC.createClient({mode:'rtc', codec:'vp8'})
let localTracks = []
let remoteUsers = {}

let joinAndDisplayLocalStream = async () => {
    client.on('user-published', handleUserJoined)

    UID = await client.join(APP_ID, CHANNEL, TOKEN, null)

    localTracks = await AgoraRTC.createMicrophoneAndCameraTracks()

    let player = `<div class="video-container" id="user-container-${UID}">
                  <div><span class="username-wrapper">My Name</span></div>
                  <div class="video-player" id="user-${UID}"></div>
                  </div>`
    document.getElementById('video-streams').insertAdjacentHTML('beforeend', player)

    localTracks[1].play(`user-${UID}`)
    await client.publish([localTracks[0], localTracks[1]])
}

let handleUserJoined = async (user, mediaType) => {
    remoteUsers[user.uid] = user
    await client.subscribe(user, mediaType)
    if(mediaType === 'video'){
        let player = document.getElementById(`user-container-${user.uid}`)
        if(player != null){
            player.remove()
        }
        player = `<div class="video-container" id="user-container-${user.uid}">
                  <div><span class="username-wrapper">My Name</span></div>
                  <div class="video-player" id="user-${user.uid}"></div>
                  </div>`
        document.getElementById('video-streams').insertAdjacentHTML('beforeend', player)
        user.videoTrack.play(`user-${user.uid}`)
    }
    if (mediaType === 'audio'){
        user.audioTrack.play()
    }
}


joinAndDisplayLocalStream()