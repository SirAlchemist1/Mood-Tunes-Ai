document.addEventListener('DOMContentLoaded', () => {
    const generateButton = document.getElementById('generateButton');
    const promptInput = document.getElementById('promptInput');
    const loadingIndicator = document.getElementById('loadingIndicator');
    const playlistResult = document.getElementById('playlistResult');
    const playlistContainer = document.getElementById('playlistContainer');

    generateButton.addEventListener('click', handleGeneratePlaylist);
    promptInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            handleGeneratePlaylist();
        }
    });

    async function handleGeneratePlaylist() {
        const prompt = promptInput.value;
        if (prompt) {
            loadingIndicator.classList.remove('hidden');
            playlistResult.classList.add('hidden');
            generateButton.disabled = true;
            try {
                const response = await fetch('/generate_playlist', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ prompt: prompt }),
                });
                const data = await response.json();
                if (data.playlist) {
                    displayPlaylist(data.playlist);
                    loadingIndicator.classList.add('hidden');
                    playlistResult.classList.remove('hidden');
                } else if (data.error) {
                    throw new Error(data.error);
                } else {
                    throw new Error('Failed to create playlist');
                }
            } catch (error) {
                console.error('Error:', error);
                alert('An error occurred while creating the playlist: ' + error.message);
                loadingIndicator.classList.add('hidden');
            } finally {
                generateButton.disabled = false;
            }
        } else {
            alert('Please enter a genre, mood, or "new music".');
        }
    }

    function displayPlaylist(playlist) {
        playlistContainer.innerHTML = '';
        playlist.forEach(track => {
            const trackElement = document.createElement('div');
            trackElement.className = 'track-item';
            trackElement.innerHTML = `
                <a href="${track.url}" target="_blank">
                    <div class="track-info">
                        <span class="track-name">${track.track}</span>
                        <span class="artist-name">${track.artist}</span>
                    </div>
                    <div class="popularity">
                        <i class="fas fa-users"></i>
                        <span>${formatNumber(track.listeners)}</span>
                    </div>
                </a>
            `;
            playlistContainer.appendChild(trackElement);
        });
    }

    function formatNumber(num) {
        if (num >= 1000000) {
            return (num / 1000000).toFixed(1) + 'M';
        } else if (num >= 1000) {
            return (num / 1000).toFixed(1) + 'K';
        }
        return num.toString();
    }
});