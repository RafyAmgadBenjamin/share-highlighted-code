<script>
	import Navigation from './Navigation.svelte';
	import hljs from 'highlight.js';
	var postHighightedCodeApiUrl =
		'http://localhost:8080/api/code/add-highlighted-code';

	hljs.initHighlightingOnLoad();

	let originalCode = '';
	let highlightedCode = { value: '' };
	function highlightCode(originalCode) {
		console.log('oringinal code', originalCode);
		highlightedCode = hljs.highlightAuto(originalCode);

		//	makeCorsRequest(postHighightedCodeApiUrl,);
		console.log('highlighted', { code: highlightedCode.value });
		postData(postHighightedCodeApiUrl, { answer: 42 })
			.then(data => console.log(data.json())) // JSON-string from `response.json()` call
			.catch(error => console.error(error));
	}

	//Copy the code
	function copyToClipboard() {
		var range = document.createRange();
		range.selectNode(document.getElementById('original-code'));
		window.getSelection().removeAllRanges(); // clear current selection
		window.getSelection().addRange(range); // to select text
		document.execCommand('copy');
		window.getSelection().removeAllRanges(); // to deselect
	}
	//Download the code3
	function downloadCode(data, fileName = 'originalCode') {
		console.log('original code', originalCode);
		var element = document.createElement('a');
		element.setAttribute(
			'href',
			'data:text/plain;charset=utf-8,' + encodeURIComponent(data)
		);
		element.setAttribute('download', fileName);
		element.style.display = 'none';
		document.body.appendChild(element);
		element.click();
		document.body.removeChild(element);
	}

	function postData(url = '', data = {}) {
		// Default options are marked with *
		return fetch(url, {
			method: 'POST', // *GET, POST, PUT, DELETE, etc.
			mode: 'cors', // no-cors, cors, *same-origin
			cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
			// credentials: 'same-origin', // include, *same-origin, omit
			headers: {
				'Content-Type': 'application/json',
				// 'Content-Type': 'application/x-www-form-urlencoded',
			},
			redirect: 'follow', // manual, *follow, error
			referrer: 'no-referrer', // no-referrer, *client
			body: JSON.stringify(data), // body data type must match "Content-Type" header
			// }).then(response => response.json()); // parses JSON response into native JavaScript objects
		});
	}
	// function createCORSRequest(method, url,data) {
	// 	var xhr = new XMLHttpRequest();
	// 	if ('withCredentials' in xhr) {
	// 		// XHR for Chrome/Firefox/Opera/Safari.
	// 		xhr.open(method, url, true);//true to make it asynchronous
	// 	} else if (typeof XDomainRequest != 'undefined') {
	// 		// XDomainRequest for IE.
	// 		xhr = new XDomainRequest();
	// 		xhr.open(method, url);
	// 		//
	// 		xhr.setRequestHeader('Content-Type', 'application/json');
	// 		xhr.send(
	// 			JSON.stringify({hamada:'hamada'})
	// 		);

	// 		//
	// 	} else {
	// 		// CORS not supported.
	// 		xhr = null;
	// 	}
	// 	return xhr;
	// }

	// // Helper method to parse the title tag from the response.
	// function getTitle(text) {
	// 	return text.match('<title>(.*)?</title>')[1];
	// }

	// // Make the actual CORS request.
	// function makeCorsRequest(url,data) {
	// 	// This is a sample server that supports CORS.

	// 	var xhr = createCORSRequest('POST', url,data);
	// 	if (!xhr) {
	// 		alert('CORS not supported');
	// 		return;
	// 	}

	// 	// Response handlers.
	// 	xhr.onload = function() {
	// 		var text = xhr.responseText;
	// 		// var title = getTitle(text);
	// 		// alert('Response from CORS request to ' + url + ': ' + title);
	// 		console.log("response",xhr.responseText)
	// 	};

	// 	xhr.onerror = function() {
	// 		alert('Woops, there was an error making the request.');
	// 	};

	// 	xhr.send();
	// }

	// Example POST method implementation:
</script>

<div>
	<Navigation />
</div>

<!--[Container]-->
<div class="container">
	<!--[Title]-->
	<div class="m-3 text-center">
		<h1>
			Shareable
			<span class="badge badge-primary">Highlighted</span>
			Code
		</h1>
	</div>
	<div class="row">
		<!--[Left-Side]-->
		<div class="col-sm-6">
			<!--[Content]-->
			<div class="row">
				<div class="col-sm-12">
					<textarea
						id="original-code"
						rows="20"
						cols="56"
						bind:value={originalCode} />
				</div>
			</div>
			<!--[BTNs]-->
			<div class="_row d-flex justify-content-between mt-4">
				<!--[Submit-BTN]-->
				<div class="_col-sm-4">
					<button
						type="button"
						on:click={() => highlightCode(originalCode)}
						class="btn btn-dark btn-lg">
						Submit
					</button>
				</div>
				<!--[Download-BTN]-->
				<div class="_col-sm-4">
					<button
						type="button"
						class="btn btn-dark btn-lg"
						on:click={() => downloadCode(originalCode)}>
						Download
					</button>
				</div>
				<!--[Submit-Copy]-->
				<div class="_col-sm-4">
					<button
						class="btn btn-dark btn-lg"
						on:click={() => copyToClipboard()}>
						<i class="far fa-copy" />
					</button>
				</div>
			</div>
		</div>
		<!--[Right-Side]-->
		<div class="col-sm-6">
			<!--[Highlighted-Code]-->
			{#if highlightedCode.value}
				<pre>
					<code class="hljs">
						{@html highlightedCode.value}
					</code>
				</pre>
			{/if}
		</div>
	</div>

</div>
