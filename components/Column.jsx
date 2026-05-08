import JobCard from "./JobCard";

export default function Column({ title, status, jobs, moveJob }) {
  const filteredJobs = jobs.filter(job => job.status === status);

  return (
    <div style={{ flex: 1, padding: "10px", border: "1px solid #ccc" }}>
      <h3>{title}</h3>

      {filteredJobs.map(job => (
        <JobCard key={job.id} job={job} moveJob={moveJob} />
      ))}
    </div>
  );
}