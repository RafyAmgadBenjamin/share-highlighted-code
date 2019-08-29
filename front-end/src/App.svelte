<script>
	import Navigation from './Navigation.svelte';
	import hljs from 'highlight.js';
	hljs.initHighlightingOnLoad();

</script>

<div>
	<Navigation />
</div>

<!--[Container]-->
<div class="container">
	<!--[Title]-->
	<div class="mt-3">
		<h1>Sharable highlited code</h1>
	</div>
	<div class="row">
		<!--[Left-Side]-->
		<div class="col-sm-6">
			<!--[Content]-->
			<div class="row">
				<div class="col-sm-12">
					<textarea rows="20" cols="50">
						At w3schools.com you will learn how to make a website. We offer free
						tutorials in all web development technologies.
					</textarea>
				</div>
			</div>
			<!--[BTNs]-->
			<div class="row">
				<!--[Submit-BTN]-->
				<div class="col-sm-4">
					<button type="button" class="btn btn-dark">Submit</button>
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

			<pre>
				<code class="javascript">var test;alert(1+1);</code>
			</pre>
			<pre>
				<code class="python">
					def add_Url(originalUrl): 
					generatedVal = str(generate_random_no())
					add_url_redis(tinyUrl=generatedVal, originalUrl=originalUrl)
					response.headers['Content-Type'] = 'application/json'
					response.headers['Cache-Control'] = 'no-cache' return
				</code>
			</pre>

		</div>
	</div>

</div>
