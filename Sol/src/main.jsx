import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import { createBrowserRouter, RouterProvider,} from 'react-router-dom'
import './index.css'
/* existing imports */
import Root from "./routes/root";
import ErrorPage from "./pages/ErrorPage";
import HomePage from "./pages/HomePage";
import AnomaliesPage from "./pages/AnomaliesPage";
import ControlCenterPage from "./pages/ControlCenterPage";
import AnalyticsPage from './pages/AnalyticsPage'

const router = createBrowserRouter([
  {
    path: "/",
    element: <Root />,
    errorElement: <ErrorPage />,
  },
  {
    path: "home/",
    element: <HomePage />,
    errorElement: <ErrorPage />,
  },
  {
    path: "anomalies/",
    element: <AnomaliesPage />,
    errorElement: <ErrorPage />,
  },

  {
    path: "control-center/",
    element: <ControlCenterPage />,
    errorElement: <ErrorPage />,
  },

  {
    path: "Analytics/",
    element: <AnalyticsPage />,
    errorElement: <ErrorPage />,
  }


]);

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);



