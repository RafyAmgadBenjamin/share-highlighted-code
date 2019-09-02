<script>
	import HighlightedCode from './HighlightedCode.svelte';
	import axios from 'axios';

	let highlightedCode = { value: '' };
	export let params;
	if (params && params.codeId != null && params.codeId != undefined) {
		getSharedCode(params.codeId);
	}

	function getSharedCode(codeId) {
		axios
			.get('http://localhost:8080/api/code/get-shared-code/' + codeId)
			.then(function(response) {
				// handle success
				console.log("respose from axios",response);
				//call hiighlitedCode
				highlightCode(response.data);
			})
			.catch(function(error) {
				// handle error
				console.log(error);
			})
			.finally(function() {
				// always executed
			});
	}

	function highlightCode(originalCode) {
		console.log('oringinal code', originalCode);
		highlightedCode = hljs.highlightAuto(originalCode);
	}
</script>

<div>
	<h1>The shared code</h1>
	<HighlightedCode {highlightedCode} />
</div>
