<div align="center">

  <!-- AAA Game AI FSM Debugger HUD Banner -->
  <img src="assets/cinematic_ai_fsm_banner.jpg" width="100%" alt="Sentinel AI Finite State Machine Debugger" style="border-radius: 12px;" />

  <br/><br/>

  <!-- Live Typing Header -->
  <a href="https://git.io/typing-svg">
    <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=22&pause=1200&color=00F0FF&center=true&vcenter=true&width=750&height=50&lines=SENTINEL_AI_FSM_v2.4+%7C+OXON+Game+Lab;ROLE%3A+Game+Designer+%26+Systems+Architect+%40+OXON;FEATURE%3A+Real-Time+Finite+State+Machine+Debugger;C%23+%7C+Unity+%7C+State+Pattern+%7C+NavMesh+AI" alt="Game AI FSM Typing SVG" />
  </a>

  <br/><br/>

  <!-- Quick Badges -->
  <p align="center">
    <a href="mailto:ingortigno@gmail.com"><img src="https://img.shields.io/badge/AI_CONSOLE-ingortigno%40gmail.com-00F0FF?style=for-the-badge&logo=gmail&logoColor=black" /></a>
    <a href="https://linkedin.com/in/cerengor" target="_blank"><img src="https://img.shields.io/badge/LINKEDIN-Ceren_Gör-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" /></a>
    <a href="https://github.com/cerogamedev"><img src="https://img.shields.io/badge/GITHUB-cerogamedev-181717?style=for-the-badge&logo=github&logoColor=white" /></a>
  </p>

</div>

<br/>

> *"Game AI is not about beating the player — it is the choreography of tension, reaction, and dynamic pacing."*

---

## 🧠 REAL-TIME GAME AI STATE MACHINE SIMULATOR

```gcode
========================================================================================
[AI CONTROLLER]: SENTINEL_FSM_v2.4 // ACTIVE STATE: ⚡ [CHASE] ⚡
[LAST TRIGGER]: Handled command by @cerogamedev at 2026-07-27 11:50:30 UTC
========================================================================================
 [PATROL] -------(Player Spotted)------> [ALERT] --------(Target Locked)------> [>>> CHASE <<<]
    ^                                                                            |
    |                                                                            v
 [IDLE] <-------(Target Lost)----------- [SEARCH] <------(Damage Taken)------- [ATTACK]
========================================================================================
```

<div align="center">

### 🔘 INTERACTIVE AI STATE CONTROLLER (CLICK TO TRIGGER)
*Click any interactive button below to trigger a real-time state transition on this profile!*

<p align="center">
  <a href="https://github.com/cerogamedev/cerogamedev/issues/new?title=fsm:patrol&body=Triggering+AI+State+Transition+to+PATROL"><img src="https://img.shields.io/badge/TRIGGER-PATROL_STATE-FF007F?style=for-the-badge&logo=target&logoColor=white"/></a>
  <a href="https://github.com/cerogamedev/cerogamedev/issues/new?title=fsm:alert&body=Triggering+AI+State+Transition+to+ALERT"><img src="https://img.shields.io/badge/TRIGGER-ALERT_STATE-FFA500?style=for-the-badge&logo=alert&logoColor=white"/></a>
  <a href="https://github.com/cerogamedev/cerogamedev/issues/new?title=fsm:chase&body=Triggering+AI+State+Transition+to+CHASE"><img src="https://img.shields.io/badge/TRIGGER-CHASE_STATE-00F0FF?style=for-the-badge&logo=zap&logoColor=black"/></a>
  <a href="https://github.com/cerogamedev/cerogamedev/issues/new?title=fsm:attack&body=Triggering+AI+State+Transition+to+ATTACK"><img src="https://img.shields.io/badge/TRIGGER-ATTACK_STATE-FF0000?style=for-the-badge&logo=crosshair&logoColor=white"/></a>
  <a href="https://github.com/cerogamedev/cerogamedev/issues/new?title=fsm:search&body=Triggering+AI+State+Transition+to+SEARCH"><img src="https://img.shields.io/badge/TRIGGER-SEARCH_STATE-9D4EDD?style=for-the-badge&logo=search&logoColor=white"/></a>
  <a href="https://github.com/cerogamedev/cerogamedev/issues/new?title=fsm:idle&body=Triggering+AI+State+Transition+to+IDLE"><img src="https://img.shields.io/badge/TRIGGER-RESET_IDLE-8B949E?style=for-the-badge&logo=power&logoColor=white"/></a>
</p>

</div>

---

## 💻 GAME AI ARCHITECTURE // C# SOURCE CODE

```csharp
namespace OXON.GameDesign.AI
{
    public enum AIStateType { Idle, Patrol, Alert, Chase, Attack, Search }

    /// <summary>
    /// Core Finite State Machine Architecture for Game AI Logic in Unity
    /// Engineered by Ceren Gör (Game Designer @ OXON)
    /// </summary>
    public class SentinelAIController : MonoBehaviour
    {
        private IAIState _currentState;
        public AIStateType ActiveState { get; private; }

        [Header("AI State Nodes")]
        [SerializeField] private PatrolState _patrolState;
        [SerializeField] private ChaseState _chaseState;
        [SerializeField] private AttackState _attackState;

        private void Start()
        {
            TransitionToState(_patrolState);
        }

        public void TransitionToState(IAIState newState)
        {
            _currentState?.OnExit(this);
            _currentState = newState;
            _currentState?.OnEnter(this);
            ActiveState = newState.Type;
            
            Debug.Log($"[SENTINEL AI]: State Transited -> {ActiveState}");
        }
    }
}
```

---

## 🏛️ 3D ISOMETRIC CONTRIBUTION EXTRUSION ENGINE

<div align="center">

  <img src="profile-3d-contrib/profile-night-view.svg" width="100%" alt="Ceren's 3D Isometric Contribution Engine" />

</div>

---

## 🕹️ SYSTEM COMPONENTS & GAME DESIGN MODULES

<details>
<summary><b>📂 [Component 01]: Game Systems & Core Loops (Click to Expand)</b></summary>

<br/>

- **Core Gameplay Loops:** Moment-to-moment mechanics and long-term meta progression systems.
- **Game Economy & Balance:** Resource management, difficulty curves (pacing & flow), and mathematical balancing models.
- **Player Psychology & UX:** Responsive player input with satisfying feedback loops (Juice, Screen Shake, Audio-Visual Cues).

</details>

<details>
<summary><b>📂 [Component 02]: Technical Design & C# Architecture (Click to Expand)</b></summary>

<br/>

- **Design Patterns in Unity:** State Machines (FSM), Observer Pattern, Command Pattern, Factory Pattern, and ScriptableObject architecture.
- **Navigation & AI:** NavMesh pathfinding, AI behavior trees, and enemy decision logic.
- **Clean & Modular Code:** Extensible, clean C# codebase built for seamless developer collaboration.

</details>

<details>
<summary><b>📂 [Component 03]: Shaders & Technical Art (Click to Expand)</b></summary>

<br/>

- **ShaderLab & Technical Art:** Custom HLSL / ShaderGraph solutions for stylized rendering and gameplay VFX.
- **2D/3D Hybrid Visuals:** 2D billboard rendering and dynamic visual management within 3D environments.

</details>

---

## 🛠️ EQUIPMENT & TECH STACK

<div align="center">

| Core Hardware & Engine | Tech Stack & Frameworks |
| :--- | :--- |
| ![Unity](https://img.shields.io/badge/Unity_Engine-100000?style=for-the-badge&logo=unity&logoColor=white) | ![C#](https://img.shields.io/badge/C%23_Language-239120?style=for-the-badge&logo=c-sharp&logoColor=white) |
| ![Rider](https://img.shields.io/badge/JetBrains_Rider-000000?style=for-the-badge&logo=rider&logoColor=white) | ![Git](https://img.shields.io/badge/Git_Version_Control-F05032?style=for-the-badge&logo=git&logoColor=white) |

<br/>

`System Architecture` • `Game Balancing` • `Player Psychology` • `NavMesh AI` • `ShaderLab` • `ScriptableObjects`

</div>

---

## 🐍 CONTRIBUTION SNAKE ARENA

<div align="center">

  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/cerogamedev/cerogamedev/output/github-contribution-grid-snake-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/cerogamedev/cerogamedev/output/github-contribution-grid-snake.svg">
    <img alt="github contribution grid snake animation" src="https://raw.githubusercontent.com/cerogamedev/cerogamedev/output/github-contribution-grid-snake.svg" width="100%">
  </picture>

</div>

---

<div align="center">
  <sub>Real-Time Game AI State Machine Simulator • <b>OXON Game Studio</b> • <code>cerogamedev</code></sub>
</div>
