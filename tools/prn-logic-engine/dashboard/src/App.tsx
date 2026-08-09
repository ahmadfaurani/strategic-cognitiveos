import { useState, useEffect } from 'react'
import { BarChart, Bar, LineChart, Line, PieChart, Pie, Cell, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts'
import { Users, TrendingUp, MapPin, Activity, AlertTriangle, CheckCircle } from 'lucide-react'

// Dashboard data types
interface Candidate {
  name: string
  seat: string
  party: string
  activityLevel: 'high' | 'medium' | 'low'
  keyEvent: string
}

interface SeatStatus {
  seat: string
  candidate: string
  status: 'safe' | 'contested' | 'vulnerable'
  threatLevel: 'low' | 'medium' | 'high'
  notes: string
}

interface CoalitionData {
  name: string
  candidates: Candidate[]
  seats: SeatStatus[]
  metrics: {
    ceramahsHeld: number
    ceramahsTarget: number
    voterContacts: number
    voterContactsTarget: number
    socialMediaReach: number
    socialMediaTarget: number
    volunteerDeployment: number
    volunteerTarget: number
  }
  developments: string[]
}

// Mock data generator (will be replaced with real data from JSON)
const generateMockData = (): Record<string, CoalitionData> => ({
  pn: {
    name: 'PN',
    candidates: [
      { name: 'Muhyiddin Yassin', seat: 'N14 Pagoh', party: 'Bersatu', activityLevel: 'high', keyEvent: 'Ceramah Perdana Pagoh' },
      { name: 'Azman Ibrahim', seat: 'N09 Semerah', party: 'PAS', activityLevel: 'high', keyEvent: 'Kempen masjid' },
      { name: 'Norhayati Omar', seat: 'N23 Puteri Wangsa', party: 'Bersatu', activityLevel: 'medium', keyEvent: 'Jumpa belia' },
      { name: 'Mazlan Bujang', seat: 'N35 Pasir Raja', party: 'PAS', activityLevel: 'medium', keyEvent: 'Ceramah subuh' },
      { name: 'Ramli Mohd Nor', seat: 'N47 Kempas', party: 'Bersatu', activityLevel: 'low', keyEvent: 'Ground walkabout' },
    ],
    seats: [
      { seat: 'N14 Pagoh', candidate: 'Muhyiddin Yassin', status: 'safe', threatLevel: 'low', notes: 'PM kuat' },
      { seat: 'N09 Semerah', candidate: 'Azman Ibrahim', status: 'contested', threatLevel: 'medium', notes: 'Pertembungan 3 penjuru' },
      { seat: 'N23 Puteri Wangsa', candidate: 'Norhayati Omar', status: 'vulnerable', threatLevel: 'high', notes: 'Pengundi campuran' },
    ],
    metrics: {
      ceramahsHeld: 15,
      ceramahsTarget: 18,
      voterContacts: 4200,
      voterContactsTarget: 5000,
      socialMediaReach: 85000,
      socialMediaTarget: 100000,
      volunteerDeployment: 950,
      volunteerTarget: 1200
    },
    developments: [
      'Muhyiddin lancar jentera di Pagoh, 1000+ hadirin',
      'PAS kempen agresif di kawasan Melayu',
      'Bersatu fokus pengundi muda'
    ]
  },
  bn: {
    name: 'BN',
    candidates: [
      { name: 'Mohamed Khaled Nordin', seat: 'N44 Permas', party: 'UMNO', activityLevel: 'high', keyEvent: 'Pelancaran jentera Iskandar Puteri' },
      { name: 'Onn Hafiz Ghazi', seat: 'N01 Machap', party: 'UMNO', activityLevel: 'high', keyEvent: 'MB gerakkan jentera' },
      { name: 'Ling Tian Soon', seat: 'N36 Tiram', party: 'MCA', activityLevel: 'medium', keyEvent: 'Kempen perindustrian' },
      { name: 'Tan Hong Pin', seat: 'N56 Kukup', party: 'MCA', activityLevel: 'medium', keyEvent: 'Jumpa nelayan' },
      { name: 'Norliza Noh', seat: 'N02 Bukit Pasir', party: 'UMNO', activityLevel: 'low', keyEvent: 'Ceramah wanita' },
    ],
    seats: [
      { seat: 'N01 Machap', candidate: 'Onn Hafiz Ghazi', status: 'safe', threatLevel: 'low', notes: 'MB incumbent' },
      { seat: 'N44 Permas', candidate: 'Mohamed Khaled Nordin', status: 'contested', threatLevel: 'medium', notes: 'Pengerusi BN' },
      { seat: 'N36 Tiram', candidate: 'Ling Tian Soon', status: 'vulnerable', threatLevel: 'high', notes: 'Pengundi campuran' },
    ],
    metrics: {
      ceramahsHeld: 8,
      ceramahsTarget: 12,
      voterContacts: 3500,
      voterContactsTarget: 5000,
      socialMediaReach: 45000,
      socialMediaTarget: 100000,
      volunteerDeployment: 800,
      volunteerTarget: 1200
    },
    developments: [
      'Khaled Nordin fokus pengundi Cina',
      'Manifesto Pemulihan Ekonomi dilancarkan',
      'MCA gerakkan jentera di 12 DUN'
    ]
  },
  ph: {
    name: 'PH',
    candidates: [
      { name: 'Aminolhuda Hassan', seat: 'N03 Pemanis', party: 'AMANAH', activityLevel: 'high', keyEvent: 'Pelancaran jentera PH' },
      { name: 'Tony Pua', seat: 'N24 Iskandar Puteri', party: 'DAP', activityLevel: 'high', keyEvent: 'Ceramah ekonomi 800+ pax' },
      { name: 'Mohd Rashid', seat: 'N25 Skudai', party: 'PKR', activityLevel: 'medium', keyEvent: 'Jumpa pengundi universiti' },
      { name: 'Lee Ting Han', seat: 'N26 Stulang', party: 'DAP', activityLevel: 'medium', keyEvent: 'Gerakkan pengundi Cina' },
      { name: 'Norhayati Omar', seat: 'N23 Puteri Wangsa', party: 'PKR', activityLevel: 'low', keyEvent: 'Kempen wanita' },
    ],
    seats: [
      { seat: 'N24 Iskandar Puteri', candidate: 'Tony Pua', status: 'safe', threatLevel: 'low', notes: 'Pengundi Cina 60%' },
      { seat: 'N25 Skudai', candidate: 'Mohd Rashid', status: 'safe', threatLevel: 'low', notes: 'Universiti' },
      { seat: 'N03 Pemanis', candidate: 'Aminolhuda Hassan', status: 'contested', threatLevel: 'medium', notes: 'Pengundi campuran' },
    ],
    metrics: {
      ceramahsHeld: 12,
      ceramahsTarget: 15,
      voterContacts: 5200,
      voterContactsTarget: 6000,
      socialMediaReach: 120000,
      socialMediaTarget: 150000,
      volunteerDeployment: 1100,
      volunteerTarget: 1500
    },
    developments: [
      'Tony Pua ceramah viral 50K+ views',
      'AMANAH cabar PN untuk undi Melayu',
      'DAP fokus pengundi Cina bandar'
    ]
  },
  independent: {
    name: 'Independent',
    candidates: [
      { name: 'Ahmad Fauzi Zakaria', seat: 'N03 Pemanis', party: 'Bebas', activityLevel: 'medium', keyEvent: 'Isu air bersih' },
      { name: 'Hassan Dollah', seat: 'N54 Pulai Sebatang', party: 'Bebas', activityLevel: 'high', keyEvent: 'Imam, 200+ hadirin' },
      { name: 'Lim Chee Wei', seat: 'N24 Senggarang', party: 'Bebas', activityLevel: 'medium', keyEvent: 'Usahawan, isu PKS' },
    ],
    seats: [
      { seat: 'N03 Pemanis', candidate: 'Ahmad Fauzi Zakaria', status: 'contested', threatLevel: 'high', notes: 'Bekas ADUN BN, 250+ undi' },
      { seat: 'N54 Pulai Sebatang', candidate: 'Hassan Dollah', status: 'contested', threatLevel: 'medium', notes: 'Imam, pengaruh agama' },
      { seat: 'N24 Senggarang', candidate: 'Lim Chee Wei', status: 'vulnerable', threatLevel: 'medium', notes: 'Pecah undi Cina' },
    ],
    metrics: {
      ceramahsHeld: 3,
      ceramahsTarget: 8,
      voterContacts: 450,
      voterContactsTarget: 1000,
      socialMediaReach: 3400,
      socialMediaTarget: 10000,
      volunteerDeployment: 85,
      volunteerTarget: 200
    },
    developments: [
      '3 bekas ADUN BN bertanding bebas',
      'Hassan Dollah (imam) paling aktif',
      'Majoriti calon "protest candidates"'
    ]
  }
})

const COLORS = {
  pn: '#16a34a',
  bn: '#f59e0b',
  ph: '#3b82f6',
  independent: '#8b5cf6'
}

function App() {
  const [data, setData] = useState<Record<string, CoalitionData> | null>(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    // In production, fetch from API endpoint
    // For now, use mock data
    setTimeout(() => {
      setData(generateMockData())
      setLoading(false)
    }, 500)
  }, [])

  if (loading) {
    return (
      <div className="dashboard" style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '100vh' }}>
        <div style={{ color: '#94a3b8' }}>Loading dashboard...</div>
      </div>
    )
  }

  if (!data) return null

  // Calculate totals
  const totalCandidates = Object.values(data).reduce((sum, c) => sum + c.candidates.length, 0)
  const totalSeats = Object.values(data).reduce((sum, c) => sum + c.seats.length, 0)
  const totalCeramahs = Object.values(data).reduce((sum, c) => sum + c.metrics.ceramahsHeld, 0)
  const totalReach = Object.values(data).reduce((sum, c) => sum + c.metrics.socialMediaReach, 0)

  // Prepare chart data
  const ceramahData = Object.values(data).map(c => ({
    name: c.name,
    Held: c.metrics.ceramahsHeld,
    Target: c.metrics.ceramahsTarget
  }))

  const reachData = Object.values(data).map(c => ({
    name: c.name,
    Reach: c.metrics.socialMediaReach
  }))

  const statusData = Object.values(data).flatMap(c => 
    c.seats.map(s => ({
      name: `${c.name} - ${s.seat}`,
      status: s.status
    }))
  )

  const statusCounts = {
    safe: statusData.filter(s => s.status === 'safe').length,
    contested: statusData.filter(s => s.status === 'contested').length,
    vulnerable: statusData.filter(s => s.status === 'vulnerable').length
  }

  const pieData = [
    { name: 'Safe', value: statusCounts.safe, color: '#22c55e' },
    { name: 'Contested', value: statusCounts.contested, color: '#f59e0b' },
    { name: 'Vulnerable', value: statusCounts.vulnerable, color: '#ef4444' }
  ]

  return (
    <div className="dashboard">
      <header className="header">
        <h1>🗳️ PRN Johor 2026 Campaign Dashboard</h1>
        <p>Real-time multi-coalition campaign intelligence tracking</p>
        <p style={{ marginTop: '0.5rem', fontSize: '0.875rem' }}>
          <strong>Report Date:</strong> 2026-06-27 | <strong>Campaign Day:</strong> D+1
        </p>
      </header>

      {/* Summary Stats */}
      <div className="stats-grid">
        <div className="stat-card">
          <h3>Total Candidates Tracked</h3>
          <div className="value">{totalCandidates}</div>
          <div className="change positive">
            <TrendingUp size={16} style={{ display: 'inline', marginRight: '4px' }} />
            Across 4 coalitions
          </div>
        </div>
        <div className="stat-card">
          <h3>Seats Analyzed</h3>
          <div className="value">{totalSeats}</div>
          <div className="change">
            <MapPin size={16} style={{ display: 'inline', marginRight: '4px' }} />
            Strategic battlegrounds
          </div>
        </div>
        <div className="stat-card">
          <h3>Ceramahs Today</h3>
          <div className="value">{totalCeramahs}</div>
          <div className="change positive">
            <Activity size={16} style={{ display: 'inline', marginRight: '4px' }} />
            High activity
          </div>
        </div>
        <div className="stat-card">
          <h3>Social Media Reach</h3>
          <div className="value">{(totalReach / 1000).toFixed(0)}K</div>
          <div className="change positive">
            <Users size={16} style={{ display: 'inline', marginRight: '4px' }} />
            Total impressions
          </div>
        </div>
      </div>

      {/* Seat Status Distribution */}
      <div className="chart-container">
        <h3>📊 Seat Status Distribution</h3>
        <ResponsiveContainer width="100%" height={300}>
          <PieChart>
            <Pie
              data={pieData}
              cx="50%"
              cy="50%"
              labelLine={false}
              label={({ name, value }) => `${name}: ${value}`}
              outerRadius={100}
              fill="#8884d8"
              dataKey="value"
            >
              {pieData.map((entry, index) => (
                <Cell key={`cell-${index}`} fill={entry.color} />
              ))}
            </Pie>
            <Tooltip />
            <Legend />
          </PieChart>
        </ResponsiveContainer>
      </div>

      {/* Coalition-by-Coalition Breakdown */}
      {Object.entries(data).map(([key, coalition]) => (
        <section key={key} className="coalition-section">
          <h2>
            <span className={`coalition-badge ${key}`}>{coalition.name}</span>
            Campaign Activity
          </h2>

          <div className="cards-grid">
            {/* Top Developments */}
            <div className="campaign-card">
              <h3>📰 Top Developments</h3>
              <ul style={{ listStyle: 'none', paddingLeft: 0 }}>
                {coalition.developments.map((dev, i) => (
                  <li key={i} style={{ marginBottom: '0.75rem', color: '#e2e8f0' }}>
                    <CheckCircle size={16} style={{ display: 'inline', marginRight: '8px', color: '#22c55e' }} />
                    {dev}
                  </li>
                ))}
              </ul>
            </div>

            {/* Key Candidates */}
            <div className="campaign-card" style={{ gridColumn: 'span 2' }}>
              <h3>👥 Key Candidate Activities</h3>
              <table className="metrics-table">
                <thead>
                  <tr>
                    <th>Candidate</th>
                    <th>Seat</th>
                    <th>Party</th>
                    <th>Activity</th>
                    <th>Key Event</th>
                  </tr>
                </thead>
                <tbody>
                  {coalition.candidates.map((candidate, i) => (
                    <tr key={i}>
                      <td style={{ fontWeight: 600 }}>{candidate.name}</td>
                      <td style={{ color: '#94a3b8' }}>{candidate.seat}</td>
                      <td>{candidate.party}</td>
                      <td>
                        <span className={`activity-indicator ${candidate.activityLevel}`}>
                          {candidate.activityLevel === 'high' ? '🔴' : candidate.activityLevel === 'medium' ? '🟡' : '🟢'}
                          {candidate.activityLevel.toUpperCase()}
                        </span>
                      </td>
                      <td style={{ color: '#94a3b8' }}>{candidate.keyEvent}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>

            {/* Seat Status */}
            <div className="campaign-card">
              <h3>🎯 Seat Status</h3>
              <table className="metrics-table">
                <thead>
                  <tr>
                    <th>Seat</th>
                    <th>Status</th>
                    <th>Threat</th>
                  </tr>
                </thead>
                <tbody>
                  {coalition.seats.map((seat, i) => (
                    <tr key={i}>
                      <td style={{ fontWeight: 600 }}>{seat.seat}</td>
                      <td>
                        <span className={`status-badge ${seat.status}`}>
                          {seat.status.toUpperCase()}
                        </span>
                      </td>
                      <td>
                        {seat.threatLevel === 'high' ? '🔴' : seat.threatLevel === 'medium' ? '🟡' : '🟢'}
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>

            {/* Metrics */}
            <div className="campaign-card" style={{ gridColumn: 'span 2' }}>
              <h3>📈 Performance Metrics</h3>
              <table className="metrics-table">
                <thead>
                  <tr>
                    <th>Metric</th>
                    <th>Achieved</th>
                    <th>Target</th>
                    <th>Progress</th>
                    <th>Status</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>Ceramahs Held</td>
                    <td>{coalition.metrics.ceramahsHeld}</td>
                    <td>{coalition.metrics.ceramahsTarget}</td>
                    <td>
                      <div style={{ width: '100%', background: '#334155', borderRadius: '4px', height: '8px' }}>
                        <div style={{ 
                          width: `${(coalition.metrics.ceramahsHeld / coalition.metrics.ceramahsTarget) * 100}%`,
                          background: coalition.metrics.ceramahsHeld >= coalition.metrics.ceramahsTarget ? '#22c55e' : '#f59e0b',
                          height: '100%',
                          borderRadius: '4px'
                        }} />
                      </div>
                    </td>
                    <td>{coalition.metrics.ceramahsHeld >= coalition.metrics.ceramahsTarget ? '✅' : '⚠️'}</td>
                  </tr>
                  <tr>
                    <td>Voter Contacts</td>
                    <td>{coalition.metrics.voterContacts.toLocaleString()}</td>
                    <td>{coalition.metrics.voterContactsTarget.toLocaleString()}</td>
                    <td>
                      <div style={{ width: '100%', background: '#334155', borderRadius: '4px', height: '8px' }}>
                        <div style={{ 
                          width: `${(coalition.metrics.voterContacts / coalition.metrics.voterContactsTarget) * 100}%`,
                          background: coalition.metrics.voterContacts >= coalition.metrics.voterContactsTarget ? '#22c55e' : '#f59e0b',
                          height: '100%',
                          borderRadius: '4px'
                        }} />
                      </div>
                    </td>
                    <td>{coalition.metrics.voterContacts >= coalition.metrics.voterContactsTarget ? '✅' : '⚠️'}</td>
                  </tr>
                  <tr>
                    <td>Social Media Reach</td>
                    <td>{(coalition.metrics.socialMediaReach / 1000).toFixed(0)}K</td>
                    <td>{(coalition.metrics.socialMediaTarget / 1000).toFixed(0)}K</td>
                    <td>
                      <div style={{ width: '100%', background: '#334155', borderRadius: '4px', height: '8px' }}>
                        <div style={{ 
                          width: `${(coalition.metrics.socialMediaReach / coalition.metrics.socialMediaTarget) * 100}%`,
                          background: coalition.metrics.socialMediaReach >= coalition.metrics.socialMediaTarget ? '#22c55e' : '#f59e0b',
                          height: '100%',
                          borderRadius: '4px'
                        }} />
                      </div>
                    </td>
                    <td>{coalition.metrics.socialMediaReach >= coalition.metrics.socialMediaTarget ? '✅' : '⚠️'}</td>
                  </tr>
                  <tr>
                    <td>Volunteer Deployment</td>
                    <td>{coalition.metrics.volunteerDeployment}</td>
                    <td>{coalition.metrics.volunteerTarget}</td>
                    <td>
                      <div style={{ width: '100%', background: '#334155', borderRadius: '4px', height: '8px' }}>
                        <div style={{ 
                          width: `${(coalition.metrics.volunteerDeployment / coalition.metrics.volunteerTarget) * 100}%`,
                          background: coalition.metrics.volunteerDeployment >= coalition.metrics.volunteerTarget ? '#22c55e' : '#f59e0b',
                          height: '100%',
                          borderRadius: '4px'
                        }} />
                      </div>
                    </td>
                    <td>{coalition.metrics.volunteerDeployment >= coalition.metrics.volunteerTarget ? '✅' : '⚠️'}</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </section>
      ))}

      {/* Ceramahs Comparison Chart */}
      <div className="chart-container">
        <h3>📊 Ceramahs: Achieved vs Target by Coalition</h3>
        <ResponsiveContainer width="100%" height={300}>
          <BarChart data={ceramahData}>
            <CartesianGrid strokeDasharray="3 3" stroke="#334155" />
            <XAxis dataKey="name" stroke="#94a3b8" />
            <YAxis stroke="#94a3b8" />
            <Tooltip 
              contentStyle={{ background: '#1e293b', border: '1px solid #334155', color: '#e2e8f0' }}
            />
            <Legend />
            <Bar dataKey="Held" fill="#22c55e" />
            <Bar dataKey="Target" fill="#f59e0b" />
          </BarChart>
        </ResponsiveContainer>
      </div>

      {/* Social Media Reach Chart */}
      <div className="chart-container">
        <h3>📱 Social Media Reach by Coalition</h3>
        <ResponsiveContainer width="100%" height={300}>
          <BarChart data={reachData}>
            <CartesianGrid strokeDasharray="3 3" stroke="#334155" />
            <XAxis dataKey="name" stroke="#94a3b8" />
            <YAxis stroke="#94a3b8" />
            <Tooltip 
              contentStyle={{ background: '#1e293b', border: '1px solid #334155', color: '#e2e8f0' }}
              formatter={(value: number) => `${(value / 1000).toFixed(0)}K`}
            />
            <Legend />
            <Bar dataKey="Reach" fill="#3b82f6" />
          </BarChart>
        </ResponsiveContainer>
      </div>

      {/* Risk Alert Section */}
      <section className="coalition-section" style={{ marginTop: '3rem' }}>
        <h2 style={{ color: '#f87171' }}>
          <AlertTriangle size={24} />
          High Priority Risks
        </h2>
        <div className="cards-grid">
          <div className="campaign-card" style={{ border: '1px solid #ef4444' }}>
            <h3 style={{ color: '#f87171' }}>🔴 PN: Undi Melayu Terpecah</h3>
            <p style={{ color: '#e2e8f0', marginTop: '0.5rem' }}>
              Calon bebas di beberapa DUN mungkin pecah undi Melayu, bantu PH menang pertembungan 3-cornered.
            </p>
          </div>
          <div className="campaign-card" style={{ border: '1px solid #ef4444' }}>
            <h3 style={{ color: '#f87171' }}>🔴 BN: Undi Cina Rendah</h3>
            <p style={{ color: '#e2e8f0', marginTop: '0.5rem' }}>
              Pengundi Cina menunjukkan minat rendah. Perlu jumpa persatuan, fokus isu ekonomi.
            </p>
          </div>
          <div className="campaign-card" style={{ border: '1px solid #ef4444' }}>
            <h3 style={{ color: '#f87171' }}>🔴 PH: Pengundi Melayu Swing</h3>
            <p style={{ color: '#e2e8f0', marginTop: '0.5rem' }}>
              Risiko pengundi Melayu swing ke PN. Tonjolkan calon AMANAH, isu agama progresif.
            </p>
          </div>
        </div>
      </section>

      <footer style={{ marginTop: '3rem', paddingTop: '2rem', borderTop: '1px solid #334155', color: '#94a3b8', textAlign: 'center' }}>
        <p><strong>Classification:</strong> TLP:AMBER - For Internal War Room Use Only</p>
        <p style={{ marginTop: '0.5rem' }}>
          Data Source: PRN-Johor-2026-H Repository | Last Updated: 2026-06-27 16:30:00
        </p>
      </footer>
    </div>
  )
}

export default App
