import { useState } from "react";
import axios from "axios";

import UploadBox from "../components/UploadBox";
import SimilarityCard from "../components/SimilarityCard";
import TopicPieChart from "../components/TopicPieChart";
import PolicyShiftChart from "../components/PolicyShiftChart";

function Dashboard() {
  const [file1, setFile1] = useState(null);
  const [file2, setFile2] = useState(null);

  const [similarity, setSimilarity] = useState(0);

  const [policyData, setPolicyData] = useState([]);

  const [topicData, setTopicData] = useState([]);

  const handleCompare = async () => {

    if (!file1 || !file2) {
      alert("Upload both PDFs");
      return;
    }

    const formData = new FormData();

    formData.append("file1", file1);
    formData.append("file2", file2);

    const response = await axios.post(
      "http://127.0.0.1:8000/compare-manifestos",
      formData
    );

    const result = response.data;

    setSimilarity(result.similarity_score);

    const shifts = Object.entries(
      result.policy_shifts
    ).map(([topic, values]) => ({
      topic,
      change: values.change
    }));

    setPolicyData(shifts);

    const topics = Object.entries(
      result.policy_shifts
    ).map(([topic, values]) => ({
      name: topic,
      value: values.new
    }));

    setTopicData(topics);
  };

  return (
    <div style={{ padding: "40px" }}>
      <h1>
        Manifesto Comparison Engine
      </h1>

      <div
        style={{
          display: "flex",
          gap: "20px",
          marginTop: "20px"
        }}
      >
        <UploadBox
          label="Manifesto 1"
          onChange={(e) =>
            setFile1(e.target.files[0])
          }
        />

        <UploadBox
          label="Manifesto 2"
          onChange={(e) =>
            setFile2(e.target.files[0])
          }
        />
      </div>

      <button
        onClick={handleCompare}
        style={{
          marginTop: "20px",
          padding: "10px 20px"
        }}
      >
        Compare
      </button>

      <div style={{ marginTop: "30px" }}>
        <SimilarityCard
          similarity={similarity}
        />
      </div>

      <div
        style={{
          display: "flex",
          gap: "50px",
          marginTop: "40px"
        }}
      >
        <TopicPieChart
          data={topicData}
        />

        <PolicyShiftChart
          data={policyData}
        />
      </div>
    </div>
  );
}

export default Dashboard;