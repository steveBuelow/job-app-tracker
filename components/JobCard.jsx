export default function JobCard({ job, moveJob }) {
  return (
    <div style={{ padding: "10px", margin: "10px 0", background: "#eee" }}>
      <p>{job.title}</p>

      <button onClick={() => moveJob(job.id, "applied")}>Applied</button>
      <button onClick={() => moveJob(job.id, "interview")}>Interview</button>
      <button onClick={() => moveJob(job.id, "offer")}>Offer</button>
    </div>
  );
}