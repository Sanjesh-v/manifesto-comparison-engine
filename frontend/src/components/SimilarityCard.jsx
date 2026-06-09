function SimilarityCard({ similarity }) {
  return (
    <div
      style={{
        textAlign: "center",
        border: "1px solid #ccc",
        padding: "20px",
        borderRadius: "10px"
      }}
    >
      <h2>Similarity Score</h2>

      <h1>{similarity}%</h1>
    </div>
  );
}

export default SimilarityCard;