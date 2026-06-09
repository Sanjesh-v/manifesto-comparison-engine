function UploadBox({ label, onChange }) {
  return (
    <div style={{
      border: "1px solid #ccc",
      padding: "20px",
      borderRadius: "10px"
    }}>
      <h3>{label}</h3>

      <input
        type="file"
        accept=".pdf"
        onChange={onChange}
      />
    </div>
  );
}

export default UploadBox;