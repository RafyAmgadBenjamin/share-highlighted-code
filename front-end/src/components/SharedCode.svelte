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
                //call highlitedCode
                
                //Get the orginal code from the response to be highlighted
				let actualCode = response.data.code;
				highlightCode(actualCode);
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
		highlightedCode = hljs.highlightAuto(originalCode);
	}
</script>

<div>
	<h1>The shared code</h1>
	<HighlightedCode {highlightedCode} />
</div>
