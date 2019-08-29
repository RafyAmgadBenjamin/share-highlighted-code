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
					<textarea rows="20" cols="50" bind:value={originalCode} />
				</div>
			</div>
			<!--[BTNs]-->
			<div class="row">
				<!--[Submit-BTN]-->
				<div class="col-sm-4">
					<button
						type="button"
						on:click={() => highlightCode(originalCode)}
						class="btn btn-dark">
						Submit
					</button>
				</div>
				<!--[Download-BTN]-->
				<div class="col-sm-4">
					<button type="button" class="btn btn-dark">Download</button>
				</div>
				<!--[Submit-Copy]-->
				<div class="col-sm-4">
					<button type="button" class="btn btn-dark">Copy</button>
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
