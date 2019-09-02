<script>
	import hljs from 'highlight.js';
	import axios from 'axios';
	import HighlightedCode from './HighlightedCode.svelte';
	var postHighightedCodeApiUrl =
		'http://localhost:8080/api/code/add-highlighted-code';

	hljs.initHighlightingOnLoad();
	let shareableUrl = '';

	let originalCode = '';
	let highlightedCode = { value: '' };
	function highlightCode(originalCode) {
		highlightedCode = hljs.highlightAuto(originalCode);
		axios
			.post(postHighightedCodeApiUrl, {
				code: originalCode,
			})
			.then(function(response) {
				shareableUrl = 'http://localhost:5000/#/share/' + response.data;
			})
			.catch(function(error) {
			});
	}

	//Copy the code
	function copyToClipboard(elementId) {
		var range = document.createRange();
		range.selectNode(document.getElementById(elementId));
		window.getSelection().removeAllRanges(); // clear current selection
		window.getSelection().addRange(range); // to select text
		document.execCommand('copy');
		window.getSelection().removeAllRanges(); // to deselect
	}
	//Download the code3
	function downloadCode(data, fileName = 'originalCode') {
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
</script>

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
					on:click={() => copyToClipboard('original-code')}>
					<i class="far fa-copy" />
				</button>
			</div>
		</div>
		<!--[Sharabe-Link]-->
		{#if shareableUrl != ''}
			<div class="row">
				<div class="col-sm-12">
					<div class="d-flex mt-5 align-items-center">
						<!--[Display-URL]-->
						<div id="shareable-url">{shareableUrl}</div>
						<div>
							<!--[Copy-BTN]-->
							<button
								class="btn btn-grey ml-3"
								on:click={() => copyToClipboard('shareable-url')}>
								<i class="far fa-copy" />
							</button>
						</div>
					</div>
				</div>
			</div>
		{/if}

	</div>
	<!--[Right-Side]-->
	<div class="col-sm-6">
		<HighlightedCode {highlightedCode} />
	</div>
</div>
