<script>
	import Navigation from './Navigation.svelte';
	// import marked from 'marked';

	import hljs from 'highlight.js';
	hljs.initHighlightingOnLoad();

	let originalCode = '';
	let highlightedCode = { value: '' };
	function highlightCode(originalCode) {
		console.log('oringinal code', originalCode);
		highlightedCode = hljs.highlightAuto(originalCode);

		console.log('highlighted', highlightedCode);
	}
	function copyToClipboard() {
		var range = document.createRange();
		range.selectNode(document.getElementById('original-code'));
		window.getSelection().removeAllRanges(); // clear current selection
		window.getSelection().addRange(range); // to select text
		document.execCommand('copy');
		window.getSelection().removeAllRanges(); // to deselect
	}
	function downloadCode(data,fileName = "originalCode") {
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
</script>

<div>
	<Navigation />
</div>

<!--[Container]-->
<div class="container">
	<!--[Title]-->
	<div class="m-3 text-center">
		<h1>Sharable highlited code</h1>
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
			{#if highlightedCode.value}
				<pre>
					<code class="hljs">
						{@html highlightedCode.value}
					</code>
					<!-- <div class="_javascript"> {codeData}</div> -->
				</pre>
			{/if}
		</div>
	</div>

</div>
