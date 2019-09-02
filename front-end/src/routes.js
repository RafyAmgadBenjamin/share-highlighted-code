import OriginalCode from './components/OriginalCode.svelte';

// import NotFound from './routes/NotFound.svelte';

let routes
routes = new Map()
routes.set('/', OriginalCode)


// routes.set('/single-worker-tasks/:taskId', SingleWorkerTasks)
// Catch-all, must be last
// routes.set('*', NotFound)

export default routes
