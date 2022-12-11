const APP_ID = '74db7ea6b53941d5aba1c335903798da'
const CHANNEL = 'main'
const TOKEN = '007eJxTYHCKXNWzhHdyg9S0CVNPyjOHljZ8PHpSPzB+4wXObqenl9oUGMxNUpLMUxPNkkyNLU0MU0wTkxINk42NTS0NjM0tLVIST0fOTG4IZGTYUjyBiZEBAkF8FobcxMw8BgYAR1EfvQ=='
let UID;

const client = AgoraRTC.createClient({mode:'rtc', codec:'vp8'})
let localTracks = []
let remoteUser = {}

let joinAndDisplayLocalStream = async () => {
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

joinAndDisplayLocalStream()