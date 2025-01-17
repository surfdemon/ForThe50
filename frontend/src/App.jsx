import Report from "./components/Report";
import NotFound from "./pages/NotFound";
import Forbidden403 from "./pages/Forbidden403";
import ServerError from './pages/ServerError';

function App() {
  return (
    <div>
      <Report />
      <NotFound />
      <Forbidden403 />
      <ServerError />
    </div>
  );
}

export default App;
