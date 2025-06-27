import React, { useEffect, useState } from "react";
import RankTable from "../components/RankTable/RankTable";

function Home() {
  const [ranks, setRanks] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8000/api/rank")
      .then((res) => res.json())
      .then((data) => setRanks(data))
      .catch((err) => console.error("Fetch rank error:", err));
  }, []);

  return (
    <div className="max-w-4xl mx-auto mt-6">
      <RankTable ranks={ranks} />
    </div>
  );
}

export default Home;
