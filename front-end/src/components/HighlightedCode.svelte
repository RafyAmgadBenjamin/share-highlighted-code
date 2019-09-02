<script>
	export let highlightedCode;
</script>

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
